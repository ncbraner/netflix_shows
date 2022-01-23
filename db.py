from sqlmodel import Session, SQLModel, create_engine
from config import settings

engine = create_engine(settings.mysql_url)
SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
