from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


__base = declarative_base()
__session = None
__engine = None

def init_env(env=None):
    from app.config import config_by_name
    global __engine
    global __session

    config = config_by_name[env or "test"]
    __engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

    Session = sessionmaker(bind=__engine)
    __session = Session()

    return config


