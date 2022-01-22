import pandas as pd

from models.content_model import update_title_by_id, get_content_by_id, get_content_list
from models.actor_model import get_actor_id_by_movie_id, get_actor_names
from models.director_model import get_director_names, get_director_id_by_movie_id
from models.category_model import get_actor_names, get_actor_id_by_movie_id
from models.country_model import get_country_names, get_country_id_by_movie_id
from pydantic_schema import WholeContentRecord


def assemble_whole_record(content_id):
    base_content = get_content_by_id(content_id)
    actors_id_in_movie = get_actor_id_by_movie_id(content_id)
    actor_names = get_actor_names(actors_id_in_movie)
    directors_id_in_movie = get_director_id_by_movie_id(content_id)
    director_names = get_director_names(directors_id_in_movie)
    category_id_in_movie = get_actor_id_by_movie_id(content_id)
    category_names = get_actor_names(category_id_in_movie)
    country_id_in_movie = get_country_id_by_movie_id(content_id)
    country_names = get_country_names(country_id_in_movie)

    return WholeContentRecord(type=base_content.type,
                              title=base_content.title,
                              directors=','.join(director_names),
                              cast=','.join(actor_names),
                              country=','.join(country_names),
                              date_added=base_content.date_added,
                              release_year=base_content.release_year,
                              rating=base_content.rating,
                              duration=base_content.duration,
                              listed_in=','.join(category_names),
                              description=base_content.description
                              )


def change_content_title(content_id, title):
    base_content = get_content_by_id(content_id)
    base_content.title = title
    update_title_by_id(base_content)
    return assemble_whole_record(content_id)


def aggragate_the_data(offset, limit):
    content = get_content_list(offset, limit)
    columns = ['title', 'id', 'release_year']
    contentdf = pd.DataFrame(content, columns=columns).drop(['id', 'title'], axis=1).describe().to_dict()
    return contentdf
