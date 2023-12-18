from django.db import models
from account.models import AssemblyUser,AssemblyUserGroup
# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    sender = models.ForeignKey(AssemblyUser,null=True,blank=True,on_delete=models.CASCADE)
    receiver = models.ManyToManyField(AssemblyUserGroup,null=True,blank=True)

    def __str__(self):
        return self.title

