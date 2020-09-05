from flask_restplus import Namespace, fields

new_customer_dict = {
    'salutation': fields.String(required=False, description='customer salutation'),
    'title': fields.String(required=False, description='customer tile (Dr. Prof, etc)'),
    'firstname': fields.String(required=True, description='customer first name'),
    'lastname': fields.String(required=True, description='customer last name'),
    'email': fields.String(required=True, description='customer email address'),
    'mobile': fields.String(required=False, description='customer cell phone number'),
    'username': fields.String(required=True, description='customer username '),
    'password': fields.String(required=False, description='customer password'),
    'avatar': fields.Raw(required=False, description='customer avatar')
}


class CustomerDto:
    api = Namespace('customer', description='Customer related operations')
    new_customer = api.model('customer', new_customer_dict)
    existing_customer = api.model('customer', dict(
        {'id': fields.Integer(required=True, description='customer id')},
        **new_customer_dict)
                                  )


# class ExistingCustomerDto:
#     api = Namespace('customer', description='customer related operations')
#     customer = api.model('customer', new_customer_dict.update({
#         'id': fields.Integer(required=False,
#                              description=('customer id, providing id is required for editing '
#                                           'an existing customer'))}),
#                          )


class BusinessDto:
    api = Namespace('business', description='Business related operations')
    business = api.model('business', {
        'id': fields.Integer(required=False,
                             description=('business id, providing id is required for editing '
                                          'an existing business')),
        'customerid': fields.Integer(required=True,
                                     description='The customer handling this business'),
        'consultantid': fields.Integer(required=False,
                                       description='The tax consultant id for this business'),
        'name': fields.String(required=True,
                              description='Name of the business'),
        'email': fields.String(required=False,
                               description='Email of the business'),
        'phone': fields.String(required=False,
                               description='Phone number of the business'),
        'web': fields.String(required=False,
                             description='Web address of the business'),
        'type': fields.String(required=False,
                              description='Type of the business'),
        'categoryid': fields.Integer(required=False,
                                     description='The id of the category of the business'),
        'peridicalsend': fields.Boolean(required=False,
                                        description=('Should the reports be send periodically '
                                                     'to the tax consultant')),
        'peridicaldate': fields.Boolean(required=False,
                                        description='time of next automatic report send')
    })
