from sqlmodel import select
from db import get_session
from sql_model_schemas import categories
from sql_model_schemas import movie_category_to_movie


def get_actor_names(ids):
    with get_session() as session:
        statement = select(categories.name).where(categories.id.in_(ids))
        category_names = session.exec(statement).all()
        return category_names


def get_actor_id_by_movie_id(content_id):
    with get_session() as session:
        statement = select(movie_category_to_movie.movie_category).where(movie_category_to_movie.content_id == content_id)
        category_ids = session.exec(statement).all()
        return category_ids

