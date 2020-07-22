import pytest
from auth_user.models.user import User
from auth_user.factory import UserFactory


@pytest.fixture()
def user():
    user = UserFactory()
    user.set_password('pavan')
    user.save()
    return user