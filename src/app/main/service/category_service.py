import datetime
from ..model.category import Category
from .. import db


def get_all_categories():
    return Category.query.all()


def get_category_by_type(category_type):
    return Category.query.filter_by(categorytype=category_type).all()


def delete_category(category_id):
    try:
        Category.query.filter_by(id=category_id).delete()
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Category successfully deleted.'
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': f'{e}',
        }
        return response_object, 409


def add_new_category(data):
    category = Category.query.filter_by(name=data['name'],
                                        categorytype=data['categorytype']).first()
    if not category:
        new_category = Category(
            lastmodified=datetime.datetime.utcnow(),
            created=datetime.datetime.utcnow(),
            categorytype=data['categorytype'],
            name=data['name']
        )
        save_changes_new_category(new_category)
        response_object = {
            'status': 'success',
            'message': 'Category successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'This category already exists',
        }
        return response_object, 409


def save_changes_new_category(new_category: Category):
    db.session.add(new_category)
    db.session.commit()


def edit_category(category_id, data: dict):
    try:
        new_category = dict(
            id=category_id,
            lastmodified=datetime.datetime.utcnow(),
            categorytype=data['categorytype'],
            name=data['name']
        )
        save_changes_edit_category(new_category)
        response_object = {
            'status': 'success',
            'message': 'Successfully edited.'
        }
        return response_object, 201

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': f'could not edit: {str(e)}'
        }
        return response_object, 409


def save_changes_edit_category(new_data_dict: dict):
    db.session.query(Category).filter_by(id=new_data_dict['id']). \
        update(new_data_dict)
    db.session.commit()
