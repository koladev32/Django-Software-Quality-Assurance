import pytest

from user.models import User


@pytest.mark.django_db
def test_user_model_creation():
    data_user = {
        "username": "koladev",
        "email": "koladev",
        "password": "12345"
    }
    
    user = User.objects.create_user(**data_user)

    assert user.username == data_user["username"]
    assert user.email == data_user["email"]

