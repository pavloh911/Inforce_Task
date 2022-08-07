import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        username="heardhunter",
        password="timetotest228",
    )
    response = client.post('/api/registration/user/', payload)
    assert response.status_code == 200
    assert 'password' not in response


@pytest.mark.django_db
def test_register_user_without_pass():
    payload = dict(
        username="heardhunter",
        password="",
    )
    response = client.post('/api/registration/user/', payload)
    assert response.status_code != 200
