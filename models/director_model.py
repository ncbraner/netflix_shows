from db import get_session
from sqlmodel import select
from sql_model_schemas import director
from sql_model_schemas import director_to_movie


def get_director_names(ids):
    with get_session() as session:
        statement = select(director.name).where(director.id.in_(ids))
        director_names = session.exec(statement).all()
        return director_names


def get_director_id_by_movie_id(director_id):
    with get_session() as session:
        statement = select(director_to_movie.director_id).where(director_to_movie.content_id == director_id)
        director_ids = session.exec(statement).all()
        return director_ids
