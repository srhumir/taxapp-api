# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from main.controller.customer_controller import api as customer_ns
from main.controller.business_controller import api as business_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API for rekloud-taxapp',
          version='1.0',
          description='The backend api for rekloud-taxapp'
          )

api.add_namespace(customer_ns, path='/customer')
api.add_namespace(business_ns, path='/business')