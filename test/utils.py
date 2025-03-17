import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from Expense_tracker.main import app
from Expense_tracker.models import Todos, Users
from Expense_tracker.routers.auth import bcrypt_context
from sqlalchemy.sql import text

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:62145090pranesh@localhost/testdb"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass = StaticPool
)



TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def override_get_current_user():
    return {'username': 'pranesh', 'id': 1, 'role': 'admin'}        



client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title= "Learn to code!",
        description ="Need to learn everyday!",
        priority = 5,
        complete = False,
        owner_id = 1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()



@pytest.fixture
def test_user():
    user = Users(
        user_name = "coding with pranesh",
        email = "coding with pranesh@gmail.com",
        first_name = "Bruce",
        last_name = " wayne",
        hashed_password = bcrypt_context.hash("testpassword"),
        role = "admin",
        phone_number = "(111)-111-1111"
    )
    
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()


__all__ = ["override_get_db", "override_get_current_user", "TestingSessionLocal", "engine"]
