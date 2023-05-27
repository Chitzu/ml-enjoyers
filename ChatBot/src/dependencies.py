from typing import AsyncGenerator
from .database import AsyncSession, async_session_maker


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

