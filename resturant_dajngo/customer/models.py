from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.conf import settings
import jwt
# Create your models here.

class User(AbstractUser):

    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=10)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # objects = UserManager

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


MENU_CHOICES = (
    ('food','FOOD'),
    ('sweet', 'SWEET'),
    ('drinks', 'DRINKS')
)

class Restaurant(models.Model):
    rest_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    Shop = models.CharField(max_length=20)
    menu = models.CharField(max_length=10, choices=MENU_CHOICES, default='food')
    price = models.FloatField()

    def __str__(self):
        return self.Shop

