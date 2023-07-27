from flask import Response, json
from services.company_service import CompanyService
import MySQLdb
from schemas.set_company_schema import SetCompanySchema
from schemas.update_company_schema import UpdateCompanySchema
from marshmallow import ValidationError
from flask_restx import Namespace, Resource, fields


company_ns = Namespace('company', description='Company operations')

company_model = company_ns.model('Company', {
    'cnpj': fields.String(required=True, description='CNPJ of the company'),
    'cnae': fields.String(required=True, description='CNAE code'),
    'company_name': fields.String(required=True, description='Company name'),
    'fantasy_name': fields.String(required=True, description='Fantasy name')
})

@company_ns.response(403, 'Forbiden')
@company_ns.response(500, 'Internal Server Error')
class CompanyController(Resource):
    def __init__(self) -> None:
        self.company_service = CompanyService()

    @company_ns.doc(description='Get a list of all companies')
    @company_ns.expect(company_ns.parser().add_argument('start', type=int, default=0, help='Start index for pagination'))
    @company_ns.expect(company_ns.parser().add_argument('limit', type=int, default=25, help='Number of items per page'))
    @company_ns.expect(company_ns.parser().add_argument('sort', type=str, help='Field to sort the results by'))
    @company_ns.expect(company_ns.parser().add_argument('dir', type=str, choices=['asc', 'desc'], help='Sort direction'))
    @company_ns.response(200, 'Ok')
    def get(self, args) -> Response:
        try:
            start = int(args.get('start', 0))
            limit = int(args.get('limit', 25))
            sort = args.get('sort')
            dir = args.get('dir', 'asc')

            companies, total_companies = self.company_service.all(start=start, limit=limit, sort=sort, dir=dir)

            response = {
                'meta': {
                    'total': total_companies
                },
                'page': {
                    'perPage': limit,
                    'currentPage': (start // limit) + 1
                },
                'data': companies
            }

            return Response(json.dumps(response), status=200, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


    @company_ns.doc(description='Create a new company')
    @company_ns.expect(company_model)
    @company_ns.response(201, 'Created')
    @company_ns.response(400, 'Bad Request')
    def post(self, payload: any) -> Response:
        try:
            schema = SetCompanySchema()
            data = schema.load(payload)
        except ValidationError as ve:
            return Response(json.dumps({'error': ve.messages}), status=400, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


        try:
            self.company_service.create(
                data["cnpj"],
                data["cnae"],
                data["company_name"],
                data["fantasy_name"],
            )

            success_response = {'message': 'Company successfully registered'}

            return Response(json.dumps(success_response), status=201, mimetype='application/json')
        except MySQLdb.IntegrityError as e:
            return Response(json.dumps({'error': "CNPJ alredy in use"}), status=400, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


@company_ns.route('/<string:cnpj>')
@company_ns.response(403, 'Forbiden')
@company_ns.response(500, 'Internal Server Error')
class CompanyByCnpjController(Resource):
    def __init__(self) -> None:
        self.company_service = CompanyService()

    @company_ns.doc(description='Get a company by CNPJ')
    @company_ns.response(200, 'OK')
    @company_ns.response(500, 'Internal Server Error')
    def get(self, cnpj: str) -> Response:
        try:
            company = self.company_service.find(cnpj)

            return Response(json.dumps(company), status=200, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


    @company_ns.doc(description='Update a company')
    @company_ns.expect(company_model)
    @company_ns.response(200, 'OK')
    @company_ns.response(400, 'Bad Request')
    def put(self, cnpj: str, payload) -> Response:
        try:
            schema = UpdateCompanySchema()
            data = schema.load(payload)
        except ValidationError as ve:
            return Response(json.dumps({'error': ve.messages}), status=400, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')

        try:
            self.company_service.update(
                cnpj,
                data["cnae"],
                data["fantasy_name"],
            )

            success_response = {'message': 'Company successfully updated'}

            return Response(json.dumps(success_response), status=200, mimetype='application/json')
        except Exception as e:

            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')
 

    @company_ns.doc(description='Delete a company by CNPJ')
    @company_ns.response(200, 'OK')
    @company_ns.response(400, 'Bad Request')
    def delete(self, cnpj: str) -> Response:
        try:
            self.company_service.remove(cnpj)

            message = {'message': 'Company successfully deleted'}

            return Response(json.dumps(message), status=200, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


company_ns.add_resource(CompanyController, '')
