from pydantic import BaseModel


class LoginReturnable(BaseModel):
    access_token: str
    token_type: str


class RegistrationReturnable(BaseModel):
    success: str = 'new user created'


class WholeContentRecord(BaseModel):
    type: str
    title: str
    directors: str
    cast: str
    country: str
    date_added: str
    release_year: str
    rating: str
    duration: str
    listed_in: str
    description: str
