# File for methods used in dja go test cases

from users.models import User


def create_user(email, password):
    return User.objects.create_user(email=email,
                                    password=password,
                                    user_type='type.regular',
                                    first_name='user',
                                    last_name='test')
