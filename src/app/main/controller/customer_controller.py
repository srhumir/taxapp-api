from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..service.customer_service import save_new_customer, edit_customer, get_all_customers, \
    get_a_customer, get_a_customer_by_email

api = CustomerDto.api
_new_customer = CustomerDto.new_customer
_existing_customer = CustomerDto.existing_customer
print(_new_customer)


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_registered_customers')
    @api.marshal_list_with(_existing_customer, envelope='data')
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.response(201, 'Customer successfully created.')
    @api.doc('create a new customer')
    @api.expect(_new_customer, validate=True)
    def post(self):
        """Creates a new customer"""
        data = request.json
        return save_new_customer(data=data)

    @api.response(201, 'Customer successfully edited.')
    @api.doc('Edit an existing customer')
    @api.expect(_existing_customer, validate=True)
    def put(self):
        """Edit an existing customer"""
        data = request.json
        return edit_customer(data=data)


@api.route('/<int:customer_id>')
@api.param('customer_id', 'The customer identifier')
@api.response(404, 'customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_new_customer)
    def get(self, customer_id):
        """get a customer given its identifier"""
        customer = get_a_customer(customer_id)
        if not customer:
            api.abort(404)
        else:
            return customer


@api.route('/<email>')
@api.param('email', 'The customer email address')
@api.response(404, 'customer not found.')
class CustomerEmail(Resource):
    @api.doc('get a customer given its email address')
    @api.marshal_with(_new_customer)
    def get(self, email):
        """get a customer given its email address"""
        customer = get_a_customer_by_email(email)
        if not customer:
            api.abort(404)
        else:
            return customer
