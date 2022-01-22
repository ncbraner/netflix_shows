from fastapi import HTTPException

from auth import AuthHandler
from models.user_model import get_user_by_username, create_user
from pydantic_schema import LoginReturnable, RegistrationReturnable
from sql_model_schemas import Users


def register_user(form_data):
    auth_handler = AuthHandler()
    user = get_user_by_username(form_data.username)

    if user:
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(form_data.password)
    new_user = Users(username=form_data.username, password=hashed_password)

    create_user(new_user)
    return RegistrationReturnable()


def login(form_data):
    auth_handler = AuthHandler()
    user = get_user_by_username(form_data.username)

    if (not user) or (not auth_handler.verify_password(form_data.password, user.password)):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user.username)

    return LoginReturnable(access_token=token, token_type="bearer")
