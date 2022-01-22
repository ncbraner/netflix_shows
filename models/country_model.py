from db import get_session
from sqlmodel import select
from sql_model_schemas import countries
from sql_model_schemas import country_to_movie


def get_country_names(ids):
    with get_session() as session:
        statement = select(countries.name).where(countries.id.in_(ids))
        country_names = session.exec(statement).all()
        return country_names


def get_country_id_by_movie_id(content_id):
    with get_session() as session:
        statement = select(country_to_movie.country_id).where(country_to_movie.content_id == content_id)
        country_ids = session.exec(statement).all()
        return country_ids
