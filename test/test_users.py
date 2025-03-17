from .utils import override_get_db, override_get_current_user,client, TestingSessionLocal
from Expense_tracker.routers.users import get_current_user,get_db
from fastapi import FastAPI, status


app = FastAPI()

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK 
    assert response.json()['user_name'] == "coding with pranesh"
    assert response.json()['email'] == "coding with pranesh@gmail.com"
    assert response.json()['first_name'] == "Bruce"
    assert response.json()['last_name'] == "wayne"
    assert response.json()['role'] == "admin"
    assert response.json()['phone_number'] == "(111)-111-1111"
    
    
def test_change_password_success(test_user):
    response = client.put("/user/password", json={"password": "testpassword",
                                                  "new_password": "newpassword"})
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    
def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={"password": "testpassword",
                                                  "new_password": "newpassword"})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}
    
    
    
    
def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/2222222222")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    