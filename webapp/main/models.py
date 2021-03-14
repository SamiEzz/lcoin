from django.db import models

from django.contrib.auth.models import User
from .managers import PersonManager

# Create your models here.
class Person(User):
    objects = PersonManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )
