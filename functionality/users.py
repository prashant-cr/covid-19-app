from flask import current_app as app

from constants.common_constants import DEFAULT_FALSE_FLAG
from models import session
from models.users import User
from passlib.hash import pbkdf2_sha256

from utils.log_handler import function_logger


@function_logger
def get_user_name_by_user_name(user_name=None):
    user_obj = session.query(User).filter(
        User.username == user_name,
        User.is_deleted == DEFAULT_FALSE_FLAG
    ).first()
    return user_obj


@function_logger
def check_user_exist(user_name=None):
    is_user_exist = get_user_name_by_user_name(
        user_name=user_name)
    if is_user_exist:
        raise ValueError("USER-ALREADY-EXIST")


@function_logger
def create_user_entry(**kwargs):
    hash_password = pbkdf2_sha256.hash(kwargs.get("password"))
    user_obj = User(
        username=kwargs.get("user_name"),
        password=hash_password,
        email=kwargs.get("email"),
        first_name=kwargs.get("first_name"),
        last_name=kwargs.get("last_name"),
        country=kwargs.get("country")
    )
    session.add(user_obj)
    session.flush()
    return user_obj


@function_logger
def create_user(**kwargs):
    check_user_exist(user_name=kwargs.get("user_name"))
    user_obj = create_user_entry(**kwargs)
    return int(user_obj.id)


