from distutils.command.upload import upload
import email
from pyexpat import model
from secrets import choice
from django.db import models

# Create your models here.
# ORM - Object Relational Mapping

class User(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    address = models.TextField(null=True,blank=True)
    pic = models.FileField(upload_to='Profile',default='profile-img.png')

    def __str__(self):
        return self.email

class Service(models.Model):

    choice = [('cleaning','cleaning'),('car cleaning','car cleaning'),('ac service','ac service')]

    provider = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=50,choices=choice)
    min_charge = models.IntegerField()
    des = models.TextField()
    area = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.provider.fname + ' > ' + self.name




