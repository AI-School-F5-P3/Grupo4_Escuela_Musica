import pytest
from fastapi.testclient import TestClient
import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from src.config.db import get_async_session
from decouple import config
from src.main import app
from src.config.db import meta

# Configurations for testing database
user= config("USER_TEST")
host= config("HOST_TEST")
password = config("PASSWORD_TEST")
db= config("DB_TEST")
port = config("PORT_TEST")

# DATABASE
DATABASE_URL_TEST = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"

# create an async engine for testing
engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
# create a session maker for testing
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
# bind the engine to the metadata
meta.bind = engine_test

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

# add the override to the app
app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    """Create and drop test database."""
    async with engine_test.begin() as conn:
        await conn.run_sync(meta.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(meta.drop_all)

# SETUP
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app) # TestClient is a class that allows you to test your FastAPI application by sending requests to it and asserting the responses.


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    ''' Fixture to create an async http client'''
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

