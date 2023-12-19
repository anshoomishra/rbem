from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class AssemblyUser(AbstractUser):
    phone_number = models.IntegerField(null=True)
    phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class AssemblyUserGroup(models.Model):
    name = models.CharField(max_length=100)
    persons = models.ManyToManyField(AssemblyUser,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic_arn = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

