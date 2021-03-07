from flask_jwt_extended import create_access_token, create_refresh_token
from passlib.hash import pbkdf2_sha256

from functionality.users import get_user_name_by_user_name
from utils.log_handler import function_logger


def is_password_match(hash_password=None, password=None):
    return pbkdf2_sha256.verify(password, hash_password)


@function_logger
def validate_user(user_name=None, password=None):
    user_obj = get_user_name_by_user_name(user_name=user_name)
    if not user_obj:
        raise ValueError("USER-RECORD-NOT-FOUND")
    password_match = is_password_match(
        hash_password=user_obj.password,
        password=password
    )
    if not password_match:
        raise ValueError("INVALID-PASSWORD")
    response_login_token = {
        'access_token': create_access_token(
            identity=int(user_obj.id)),
        'refresh_token': create_refresh_token(
            identity=int(user_obj.id))
    }
    return response_login_token
