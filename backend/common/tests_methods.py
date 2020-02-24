# File for methods used in dja go test cases

from users.models import User


def create_user(email, password):
    return User.objects.create_user(email=email,
                                    password=password,
                                    user_type=User.REGULAR,
                                    first_name='regular',
                                    last_name='test')


def create_manager(email, password):
    return User.objects.create_user(email=email,
                                    password=password,
                                    user_type=User.MANAGER,
                                    first_name='manager',
                                    last_name='test')
