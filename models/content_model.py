from sqlmodel import select
from db import get_session
from sql_model_schemas import content


def update_title_by_id(updated_content: content):
    with get_session() as session:
        session.add(updated_content)
        session.commit()


def get_content_by_id(content_id):
    with get_session() as session:
        statement = select(content).where(content.id == content_id)
        contents = session.exec(statement).first()
        return contents


def get_content_list(offset, limit):
    with get_session() as session:
        statement = select(content.title, content.id, content.release_year).offset(offset).limit(limit)
        contents = session.exec(statement).all()
        return contents
