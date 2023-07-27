from flask import Blueprint, request
from controllers.company_controller import CompanyController, CompanyByCnpjController
from controllers.auth_controller import AuthController
from utils.jwt import jwt_required

router = Blueprint('api', __name__)
company_controller = CompanyController()
company_by_cnpj_controller = CompanyByCnpjController()
auth_controller = AuthController()


@router.route('/auth/login', methods=['POST'])
def login():
    return auth_controller.login(request.get_json())

@router.route('/company', methods=['GET'])
@jwt_required
def get_companies(auth):
    return company_controller.get(request.args)

@router.route('/company/<cnpj>', methods=['GET'])
@jwt_required
def get_company(auth, cnpj = ''):
    return company_by_cnpj_controller.get(cnpj)

@router.route('/company', methods=['POST'])
@jwt_required
def set_company(auth):
    return company_controller.post(request.get_json())

@router.route('/company/<cnpj>', methods=['PUT'])
@jwt_required
def update_company(auth, cnpj = ''):
    return company_by_cnpj_controller.put(cnpj, request.get_json())

@router.route('/company/<cnpj>', methods=['DELETE'])
@jwt_required
def delete_company(auth, cnpj = ''):
    return company_by_cnpj_controller.delete(cnpj)
