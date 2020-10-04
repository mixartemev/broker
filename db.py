from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import env
from models import Base

# Create connection
engine = create_engine('mysql+mysqlconnector://{}:{}@{}/broker'.format(env.DB_USR, env.DB_PWD, env.DB_HOST), echo=False)
# Create all not created defined tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)  # , autoflush=False)
session = Session()
