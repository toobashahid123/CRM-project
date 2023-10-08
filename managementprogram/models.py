from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  blank=True)
    Name = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    emailid =models.CharField(max_length=200)
    salary =models.CharField(max_length=200,default=0)
    last_name =models.CharField(max_length=200)

    def __str__(self):
        return self.Name
    

