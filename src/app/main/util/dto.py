from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'id': fields.Integer(required=False,
                             description=('customer id, providing id is required for editing '
                                          'an existing customer')),
        'salutation': fields.String(required=False, description='customer salutation'),
        'title': fields.String(required=False, description='customer tile (Dr. Prof, etc)'),
        'firstname': fields.String(required=True, description='customer first name'),
        'lastname': fields.String(required=True, description='customer last name'),
        'email': fields.String(required=True, description='customer email address'),
        'mobile': fields.String(required=False, description='customer cell phone number'),
        'username': fields.String(required=True, description='customer username '),
        'password': fields.String(required=False, description='customer password'),
        'avatar': fields.Raw(required=False, description='customer avatar')
    })
