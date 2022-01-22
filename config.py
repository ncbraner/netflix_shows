from pydantic import BaseSettings


class Settings(BaseSettings):
    mysql_url: str = "mysql+pymysql://netflix-demo:root@34.122.76.158/netflixdemo"
    secret_key: str = 'SECRET'
