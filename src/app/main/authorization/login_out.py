from main.model.customer import Customer
from main.authorization.blacklist_service import save_token
from .encode_decode_tokens import encode_auth_token, decode_auth_token


class Auth:

    @staticmethod
    def login_customer(data):
        try:
            user = Customer.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = encode_auth_token(user.id, user.role,
                                                    user.subscription_expiration)
                if isinstance(auth_token, bytes):
                    print(auth_token, type(auth_token))
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
                else:
                    print('wromg token:', auth_token)
                    raise Exception('sth is wrong')

            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_customer(data):
        print(data)
        if data:
            auth_token = data
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    # TODO needs to be repaired. Calling db for every API call does not make sense
    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = Customer.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'role': user.role,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

