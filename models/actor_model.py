from sqlmodel import select
from db import get_session
from sql_model_schemas import actors
from sql_model_schemas import actors_to_movie


def get_actor_id_by_movie_id(conId):
    with get_session() as session:
        statement = select(actors_to_movie.actor_id).where(actors_to_movie.content_id == conId)
        actor_ids = session.exec(statement).all()
        return actor_ids


def get_actor_names(ids):
    with get_session() as session:
        statement = select(actors.name).where(actors.id.in_(ids))
        actor_names = session.exec(statement).all()
        return actor_names


class ActorModels:

    def __init__(self):
        pass
