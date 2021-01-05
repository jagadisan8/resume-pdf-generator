from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200)
    phone = models.IntegerField()
    previous_work = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
