from django.db import models
from ..account.models import AssemblyUser
from django.contrib.auth.models import Group
# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    sender = models.ForeignKey(AssemblyUser,null=True,blank=True)
    receiver = models.ForeignKey(Group,null=True,blank=True)

    def __str__(self):
        return self.title

