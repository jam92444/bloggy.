from django.db import models

class Email_Manager(models.Manager):
    def available_Email(self):
        return self.filter(is_available=True)

# Create your models here.
class Register(models.Model):
    UserName = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=255)

class myform(models.Model):
    Uname=models.CharField(max_length=150,default="")
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=150,default="")
 