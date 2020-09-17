import jwt
import datetime

from ..config import key, token_validity_in_days
from ..model.blacklist import BlacklistToken


def generate_token(user):
    try:
        auth_token = encode_auth_token(user.id, user.role, user.subscription_expiration)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def encode_auth_token(user_id: int, user_role: str, subscription_expiration: datetime.datetime
                      ) -> str or bool:
    """
    Generates the Auth Token
    :return: string
    """
    try:
        exp, role = create_token_expiration(subscription_expiration, user_role)
        payload = {
            'exp': exp,
            'iat': datetime.datetime.utcnow(),
            'sub': user_id,
            'role': role
        }
        return jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token: str) -> (int, str) or str:
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, key)
        is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
        if is_blacklisted_token:
            return 'Token blacklisted. Please log in again.'
        else:
            return payload['sub'], payload['role']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def create_token_expiration(subscription_expiration: datetime.datetime, user_role: str
                            ) -> (datetime.datetime, str):
    now = datetime.datetime.utcnow().replace(tzinfo=subscription_expiration.tzinfo)
    default_exp_time = now + datetime.timedelta(days=token_validity_in_days, seconds=5)
    if now <= subscription_expiration:
        return (min(default_exp_time, subscription_expiration + datetime.timedelta(seconds=5)),
                user_role)
    else:
        return datetime.datetime.utcnow(), 'un_payed'
