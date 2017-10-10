from django.db.models import Model
from django.db import models
from django.contrib.auth.models import User


class Dog(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return '%s - %s' % (self.name, self.birthday)


class Cat(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return '%s - %s' % (self.name, self.birthday)
