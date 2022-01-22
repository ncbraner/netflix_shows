from typing import Optional

from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str


class actors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class actors_to_movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content_id: int
    actor_id: int


class content(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: int
    title: str
    date_added: str
    release_year: str
    rating: str
    duration: str
    description: str


class country_to_movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content_id: int
    country_id: int


class countries(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class director(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class director_to_movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content_id: int
    director_id: int


class movie_category_to_movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content_id: int
    movie_category: int


class categories(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
