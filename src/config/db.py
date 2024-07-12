from typing import AsyncGenerator
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from decouple import config
# from logger import Logs


# logger = Logs()

try:
    user = config('USER')
    host= config("HOST")
    password = config("PASSWORD")
    db = config("DB")
    port = config("PORT")

    # url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
    url = f"postgresql+asyncpg://postgres:postgres@localhost:5432/MusicaRitmo"
    

    # Conection with data base... Data base is called 
    engine = create_async_engine(url, poolclass=NullPool)
    # Save the connection in a variable to use in other files
    conexion = engine.connect()
    # MetaData act like a container to save the information on the tables, columns
    # relaciones y otros elementos de la base de datos. Se utiliza para definir y manipular estructuras de la base de datos en SQLAlchemy.
    meta = MetaData()

    Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    Base = declarative_base()

    async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
        async with Session() as session:
                yield session

    
except SQLAlchemyError as e:
    # logger.error("Error to connect base data:")
    print(f"Base data connection Error: {e}")
    
    
    
