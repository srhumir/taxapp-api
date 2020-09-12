import datetime

from main import db
from ..model.customer import Customer, CustomerHistory


def save_new_customer(data):
    customer = Customer.query.filter_by(email=data['email']).first()
    if not customer:
        new_customer_dict = produce_new_customer_dict(data)
        new_customer = Customer(**new_customer_dict)
        save_changes_new_customer(new_customer)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer already exists. Please Log in.',
        }
        return response_object, 409


def produce_new_customer_dict(data: dict):
    new_customer_dict = dict(
        lastmodified=datetime.datetime.utcnow(),
        created=datetime.datetime.utcnow(),
        title=data.get('title', ''),
        salutation=data.get('salutation', ''),
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        mobile=data.get('mobile'),
        active=True,
        username=data['username'],
        password=data.get('password'),
        avatar=data.get('avatar',
                        produce_avatar_from_name(data['firstname'], data['lastname'])),
    )
    return new_customer_dict


def produce_avatar_from_name(first_name: str, last_name):
    return None


def get_all_customers():
    return Customer.query.all()


def get_a_customer(customer_id):
    return Customer.query.filter_by(id=customer_id).first()


def get_a_customer_by_email(email):
    return Customer.query.filter_by(email=email).first()


def save_changes_new_customer(data):
    db.session.add(data)
    db.session.commit()


def edit_customer(customer_id, data: dict):
    try:
        # customer_id = data['id']
        old_customer = get_a_customer(customer_id)
        last_version = old_customer.version
        new_customer_dict = produce_new_customer_dict(data)
        new_customer_dict['id'] = customer_id
        new_customer_dict['version'] = last_version + 1

        customer_for_history = CustomerHistory(
            id=customer_id,
            version=old_customer.version,
            lastmodified=datetime.datetime.utcnow(),
            created=old_customer.created,
            title=old_customer.title,
            salutation=old_customer.salutation,
            firstname=old_customer.firstname,
            lastname=old_customer.lastname,
            email=old_customer.email,
            mobile=old_customer.mobile,
            active=False,
            username=old_customer.username,
            password=old_customer.password_hash,
            avatar=old_customer.avatar
        )
        save_changes_edit_customer(customer_for_history, new_customer_dict)
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


def save_changes_edit_customer(old_data: CustomerHistory, new_data_dict: dict):
    db.session.add(old_data)
    db.session.query(Customer).filter_by(id=new_data_dict['id']). \
        update(new_data_dict)
    db.session.commit()
