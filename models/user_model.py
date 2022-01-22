from sqlmodel import select

from db import get_session
from sql_model_schemas import Users


def get_user_by_username(name):
    with get_session() as session:
        statement = select(Users).where(Users.username == name)
        user = session.exec(statement).first()
        return user


def get_user_by_id(content_id):
    with get_session() as session:
        statement = select(Users).where(Users.id == content_id)
        user = session.exec(statement).first()
        return user


def get_user_list():
    with get_session() as session:
        statement = select(Users)
        user = session.exec(statement).fetchall()
        return user


def create_user(userdata):
    with get_session() as session:
        session.add(userdata)
        session.commit()

