from sqlmodel import Session, SQLModel, create_engine
from config import Settings

engine = create_engine(Settings().mysql_url)
SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
