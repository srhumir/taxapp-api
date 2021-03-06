from flask import request
from flask_restplus import Resource

from ..util.dto import BusinessDto
from ..service.business_service import save_new_business, edit_business, get_all_businesss, \
    get_a_business, get_all_businesses_from_a_customers

api = BusinessDto.api
_business = BusinessDto.business


@api.route('/')
class BusinessList(Resource):
    @api.doc('list_of_registered_businesss')
    @api.marshal_list_with(_business, envelope='data')
    def get(self):
        """List all registered businesss"""
        return get_all_businesss()

    @api.response(201, 'Business successfully created.')
    @api.doc('create a new business')
    @api.expect(_business, validate=True)
    def post(self):
        """Creates a new business"""
        data = request.json
        return save_new_business(data=data)


@api.route('/<int:business_id>')
@api.param('business_id', 'The business identifier')
@api.response(404, 'Business not found.')
class Business(Resource):
    @api.doc('get a business')
    @api.marshal_with(_business)
    def get(self, business_id):
        """get a business given its identifier"""
        business = get_a_business(business_id)
        if not business:
            api.abort(404)
        else:
            return business

    @api.response(201, 'Business successfully edited.')
    @api.doc('Edit an existing business')
    @api.expect(_business, validate=True)
    def put(self, business_id):
        """Edit an existing business"""
        data = request.json
        return edit_business(business_id=business_id, data=data)


@api.route('/filter_by_customer/<int:customer_id>')
@api.param('customer_id', 'The customer identifier')
@api.response(404, 'Business not found.')
class Customer(Resource):
    @api.doc('get all the businesses belonging to a customer')
    @api.marshal_list_with(_business)
    def get(self, customer_id):
        """get all the businesses belonging to a customer"""
        businesses = get_all_businesses_from_a_customers(customer_id)
        if not businesses:
            api.abort(404)
        else:
            return businesses
