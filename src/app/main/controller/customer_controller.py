from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..service.customer_service import save_or_edit_customer, get_all_customers, get_a_customer

api = CustomerDto.api
_customer = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_registered_customers')
    @api.marshal_list_with(_customer, envelope='data')
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.response(201, 'Customer successfully created.' or 'Customer successfully edited.')
    @api.doc('create a new customer or edit an existing one')
    @api.expect(_customer, validate=True)
    def post(self):
        """Creates a new Customer or edit an existing one """
        data = request.json
        return save_or_edit_customer(data=data)


@api.route('/<int:customer_id>')
@api.param('customer_id', 'The customer identifier')
@api.response(404, 'customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer)
    def get(self, customer_id):
        """get a customer given its identifier"""
        customer = get_a_customer(customer_id)
        if not customer:
            api.abort(404)
        else:
            return customer
