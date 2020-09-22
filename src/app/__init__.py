# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from main.controller.customer_controller import api as customer_ns
from main.controller.business_controller import api as business_ns
from main.controller.category_controller import api as category_ns
from main.controller.auth_controller import api as login_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API for invoicia',
          version='1.0',
          description='The backend api for invoicia'
          )

api.add_namespace(customer_ns, path='/customer')
api.add_namespace(business_ns, path='/business')
api.add_namespace(category_ns, path='/category')
api.add_namespace(login_ns, path='/auth')
