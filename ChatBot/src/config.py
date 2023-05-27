from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    host: str
    port: str
    user: str
    password: str
    name: str

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"
        env_prefix = "DB_"
