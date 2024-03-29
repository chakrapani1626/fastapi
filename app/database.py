from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:admin@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@' \
                          f'{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

while True:
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin',
                                cursor_factory=RealDictCursor)

        # Open a cursor to perform database operations
        cursor = conn.cursor()

        print("Database connection was successful !")
        break
    except Exception as error:
        print("Error unable to connect to database")
        print("Error: ", error)
        time.sleep(2)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
