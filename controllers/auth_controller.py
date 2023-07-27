import json
from services.auth_service import AuthService
from flask_restx import Namespace, Resource, fields
from flask import Response

auth_ns = Namespace('auth', description='Auth operations')

auth_model = auth_ns.model('Auth', {
    'email': fields.String(required=True, description='User\'s email'),
    'password': fields.String(required=True, description='User\'s password'),
})

@auth_ns.route('/login')
class AuthController(Resource):
    def __init__(self) -> None:
        self.auth_service = AuthService()

    @auth_ns.doc(description='Login')
    @auth_ns.expect(auth_model)
    @auth_ns.response(200, 'Ok')
    @auth_ns.response(404, 'Not Found')
    @auth_ns.response(500, 'Internal Server Error')
    def login(self, payload):
        try:
            user = self.auth_service.login(
                email=payload["email"],
                password=payload["password"]
            )
            jwt_token = self.auth_service.generate_token(user["id"])

            return Response(json.dumps({'token': jwt_token}), status=200, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), status=404, mimetype='application/json')

auth_ns.add_resource(AuthController, endpoint='login')
