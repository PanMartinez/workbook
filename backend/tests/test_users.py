import json
import pytest

from common.tests_methods import create_user, create_manager

from users.models import User

pytestmark = pytest.mark.django_db


def create_payload(payload):
    return bytes(json.dumps(payload), 'utf-8')


def test_users_creation(rf):

    user = create_user(email='test@regular.wb', password='TestPassword')
    manager = create_manager(email='test@manager.wb', password='TestPassword')

    new_user = User.objects.get(email='test@regular.wb')
    assert new_user.type == User.REGULAR

    new_user = User.objects.get(email='test@manager.wb')
    assert new_user.type == User.MANAGER


