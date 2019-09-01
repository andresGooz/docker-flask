from app.models import *
from sqlalchemy import create_engine
DATABASE_URI = 'postgres+psycopg2://root:admin@postgres:5432/flask'
engine = create_engine(DATABASE_URI)

#to recreate the db every time activate.py is activated
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
