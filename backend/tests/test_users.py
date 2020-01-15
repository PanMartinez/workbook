import json
import pytest

from common.tests_methods import create_user

from users.models import User

pytestmark = pytest.mark.django_db


def create_payload(payload):
    return bytes(json.dumps(payload), 'utf-8')


def test_users_creation(rf):
    user = create_user(email='user@test.wb', password='TestPassword')

    new_user = User.objects.get(email='user@test.wb')
    assert new_user

