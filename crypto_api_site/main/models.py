from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)
    api_secret_key = models.CharField(max_length=200)
    def __str__(self):
        return self.username