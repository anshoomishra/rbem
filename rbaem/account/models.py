from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.utils import timezone
# Create your models here.

class AssemblyUserQuerySet(models.QuerySet):
    def all_verified(self):
        return self.filter(phone_verified=True)
    def all_approved(self):
        return self.filter(is_approved=True)

    def search(self,query):
        lookup = (Q(username__icontains=query) | Q(first_name__icontains=query))
        return self.filter(lookup).distinct()

class AssemblyUserManager(models.Manager):
    def all(self):
        return self.get_queryset().all()
    def get_queryset(self):
        return AssemblyUserQuerySet(model=self.model,using=self._db)

    def verified(self):
        return self.get_queryset().all_verified()

    def approved(self):
        return self.get_queryset().all_approved()

    def search(self,query):
        return self.get_queryset().search(query)


class AssemblyUser(AbstractUser):
    phone_number = models.IntegerField(null=True)
    phone_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    booth_name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.username
    objects = AssemblyUserManager()


class AssemblyUserGroup(models.Model):
    name = models.CharField(max_length=100)
    persons = models.ManyToManyField(AssemblyUser,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic_arn = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

