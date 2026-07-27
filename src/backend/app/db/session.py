from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from app.core.config import Settings

"""pool_pre_ping is used check the database connection before giving to application"""
engine = create_engine(
    Settings.database_url,
    echo = Settings.debug,
    pool_pre_ping = True
)

session_local = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False,
    expire_on_commit = False
)

def get_db() -> Generator[session, None, None]:
    database = session_local()
    
    try:
        yield database
    finally:
        database.close()