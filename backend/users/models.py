from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    """
    Define a model manager for User model with no username field.
    """

    use_in_migrations = True

    ALLOWED_FIELDS_CREATE_USER = ('first_name', 'last_name', 'user_type')

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular User with the given email and password.
        """
        clean_extra_fields = {}
        for k in self.ALLOWED_FIELDS_CREATE_USER:
            clean_extra_fields[k] = extra_fields.get(k)

        clean_extra_fields.setdefault('is_staff', False)
        clean_extra_fields.setdefault('is_superuser', False)
        clean_extra_fields.setdefault('is_active', False)

        regular_user = self._create_user(email, password, **clean_extra_fields)

        return regular_user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        new_superuser = self._create_user(email, password, **extra_fields)

        return new_superuser


class Notifications(models.Model):
    """
    Model with notifications settings
    """
    DAILY = 'type.daily'
    WEEKLY = 'type.weekly'
    MONTHLY = 'type.monthly'

    NOTIFICATION_TYPE_CHOICES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly')
    )
    notification_types = models.SmallIntegerField('notification types', choices=NOTIFICATION_TYPE_CHOICES, default=WEEKLY)
    notification_time = models.TimeField('notification time', null=True, blank=True)


class User(AbstractUser):
    """
    Custom User model with email as authentication field
    """

    class Meta:
        default_permissions = ()

    REGULAR = 'type.regular'
    MANAGER = 'type.manager'

    USER_TYPE_CHOICES = (
        (REGULAR, 'Regular'),
        (MANAGER, 'Manager'),
    )

    username = None

    email = models.EmailField('email address', unique=True)
    user_type = models.CharField('user type', max_length=32, choices=USER_TYPE_CHOICES, default=REGULAR)
    notifications = models.OneToOneField(Notifications, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
