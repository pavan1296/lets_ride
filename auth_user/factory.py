import factory
from factory import django
import datetime
import string
import factory.fuzzy
from auth_user.models.user import User

class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    phone_number = "7799888142"
    image_url = "www.google.com"
    name = "Pavan"