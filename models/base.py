from config import environments
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dictalchemy import DictableModel

url = "{}://{}:{}@{}:{}/{}".format(
    environments.dbdrive,
    environments.dbuser,
    environments.dbpassword,
    environments.dbhost,
    environments.dbport,
    environments.dbname
)
engine = create_engine(url)
Session = sessionmaker(bind=engine)

Base = declarative_base(cls=DictableModel)