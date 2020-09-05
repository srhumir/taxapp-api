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


new_business_dict = {
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
                                    description=(
                                        'Should the reports be send periodically '
                                        'to the tax consultant')),
    'peridicaldate': fields.Boolean(required=False,
                                    description='time of next automatic report send')
}


class BusinessDto:
    api = Namespace('business', description='Business related operations')
    new_business = api.model('business', new_business_dict)
    existing_business = api.model('business', dict(
        {'id': fields.Integer(required=True, description='business id')},
        **new_business_dict))
