from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:62145090pranesh@localhost/todoapp'



engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

with engine.connect() as conn:
    print("Connected to MySQL!")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()





__all__ = ["SessionLocal", "Base", "engine"]
    