from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='Customer related operations')
    customer = api.model('customer', {
        'salutation': fields.String(required=False, description='customer salutation'),
        'title': fields.String(required=False, description='customer tile (Dr. Prof, etc)'),
        'firstname': fields.String(required=True, description='customer first name'),
        'lastname': fields.String(required=True, description='customer last name'),
        'email': fields.String(required=True, description='customer email address'),
        'mobile': fields.String(required=False, description='customer cell phone number'),
        'role': fields.String(required=True,
                              description='role of customer system_admin, admin, user'),
        'username': fields.String(required=True, description='customer username '),
        'password': fields.String(required=False, description='customer password'),
        # 'avatar': fields.Raw(required=False, description='customer avatar')
    })


class BusinessDto:
    api = Namespace('business', description='Business related operations')
    business = api.model('business', {
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
    })


class CategoryDto:
    api = Namespace('category', description='category related operations')
    category = api.model('category', {
        'id': fields.Integer(required=False, descritipn='id of the category'),
        'categorytype': fields.String(required=True, descritipn='Type of the category'),
        'name': fields.String(required=True, descritipn='Name of the category'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    customer_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })