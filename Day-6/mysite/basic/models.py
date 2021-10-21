from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_id = models.EmailField(unique=True)
    