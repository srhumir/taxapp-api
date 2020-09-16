from flask import request
from flask_restplus import Resource

from ..service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
customer_auth = AuthDto.customer_auth


@api.route('/login')
class CustomerLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('customer login')
    @api.expect(customer_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.login_customer(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_customer(data=auth_header)