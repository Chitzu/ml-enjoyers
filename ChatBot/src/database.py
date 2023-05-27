from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .config import DatabaseSettings
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

db_config = DatabaseSettings()
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.name}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "auth_user"


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)