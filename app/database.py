from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
import psycopg2
import time

SQLALCHEMY_DATABASE = 'postgresql://postgres:password123@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

"""while True:

    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', 
                                password = 'password123', cursor_factory = RealDictCursor)
    
        cursor = conn.cursor()

        print ("Database connection was succesfull!")
        break

    except Exception as error:
        print ("Connection to database failed")
        print ("Error: ", error)
        time.sleep(2)
"""