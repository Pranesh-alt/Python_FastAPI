from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from Expense_tracker.database import Base
from Expense_tracker.main import app
from Expense_tracker.routers.admin import get_db, get_current_user
from fastapi.testclient import TestClient
from fastapi import status


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

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


client = TestClient(app)

def test_read_all_authenticated():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    
    