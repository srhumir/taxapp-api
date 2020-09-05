import datetime

from main import db
from ..model.business import Busines, BusinesHistory


def save_or_edit_business(data: dict):
    id = data.get('id')
    if id is None:
        return save_new_business(data)
    else:
        return edit_business(data)


def save_new_business(data):
    business = Busines.query.filter_by(customerid=data['customerid'], name=data['name']).first()
    if not business:
        new_business_dict = produce_new_business_dict(data)
        new_business = Busines(**new_business_dict)
        save_changes_new_business(new_business)
        response_object = {
            'status': 'success',
            'message': 'Business successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'This customer has a business with a same name',
        }
        return response_object, 409


def produce_new_business_dict(data: dict):
    new_business_dict = dict(
        lastmodified=datetime.datetime.utcnow(),
        created=datetime.datetime.utcnow(),
        customerid=data['customerid'],
        consultantid=data.get('consultantid'),
        name=data['name'],
        email=data.get('email'),
        phone=data.get('phone'),
        web=data.get('web'),
        type=data['type'],
        categoryid=data.get('categoryid'),
        peridicalsend=data.get('peridicalsend', False),
        peridicaldate=data.get('peridicaldate')
    )
    return new_business_dict


def get_all_businesss():
    return Busines.query.all()


def get_a_business(business_id):
    return Busines.query.filter_by(id=business_id).first()


def save_changes_new_business(data):
    db.session.add(data)
    db.session.commit()


def edit_business(data: dict):
    try:
        business_id = data['id']
        old_business = get_a_business(business_id)
        last_version = old_business.version
        new_business_dict = produce_new_business_dict(data)
        new_business_dict['id'] = business_id
        new_business_dict['version'] = last_version + 1

        business_for_history = BusinesHistory(
            id=old_business.id,
            version=old_business.version,
            lastmodified=datetime.datetime.utcnow(),
            created=old_business.created,
            customerid=old_business.customerid,
            consultantid=old_business.consultantid,
            name=old_business.name,
            email=old_business.email,
            phone=old_business.phone,
            web=old_business.web,
            type=old_business.type,
            categoryid=old_business.categoryid,
            peridicalsend=old_business.peridicalsend,
            peridicaldate=old_business.peridicaldate

        )
        save_changes_edit_business(business_for_history, new_business_dict)
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


def save_changes_edit_business(old_data: BusinesHistory, new_data_dict: dict):
    db.session.add(old_data)
    db.session.query(Busines).filter_by(id=new_data_dict['id']).\
        update(new_data_dict)
    db.session.commit()


def get_all_businesses_from_a_customers(customer_id):
    return Busines.query.filter_by(customerid=customer_id).all()
