from django.db import models
from django.contrib.auth.models import AbstractUser

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
class login_info(AbstractUser):
    username = models.CharField(max_length=255, unique = True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    security_question = models.CharField(max_length=255, default = "")
    security_answer = models.CharField(max_length=255, default = "")
    # birth_date = models.DateField()

# Explicitly declare app_label
class Meta:
    app_label = 'alpha'
