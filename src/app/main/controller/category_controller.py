from flask import request
from flask_restplus import Resource

from ..util.dto import CategoryDto
from ..service.category_service import add_new_category, edit_category, get_all_categories, \
    get_category_by_type, delete_category

api = CategoryDto.api
_category = CategoryDto.category


@api.route('/')
class CategoryList(Resource):
    @api.doc('list_of_registered_categories')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """list of created categories"""
        return get_all_categories()

    @api.response(201, 'Category successfully created.')
    @api.doc('create a new category')
    @api.expect(_category, validate=True)
    def post(self):
        """Creates a new category"""
        data = request.json
        return add_new_category(data=data)


@api.route('/<int:category_id>')
@api.param('category_id', 'The category identifier')
@api.response(404, 'category not found.')
class Category(Resource):
    @api.response(201, 'Category successfully edited.')
    @api.doc('Edit an existing category')
    @api.expect(_category, validate=True)
    def put(self, category_id):
        """Edit an existing category"""
        data = request.json
        return edit_category(category_id=category_id, data=data)

    @api.response(201, 'Category successfully deleted.')
    @api.doc('Delete an existing category')
    def delete(self, category_id):
        """Delete an existing category"""
        return delete_category(category_id=category_id)


@api.route('/<string:category_type>')
@api.param('category_type', 'The category type')
@api.response(404, 'no category was found.')
class CategoryType(Resource):
    @api.doc('get all category from a type')
    @api.marshal_with(_category)
    def get(self, category_type):
        """get all categories from a type"""
        categories = get_category_by_type(category_type)
        if not categories:
            api.abort(404)
        else:
            return categories
