from django.db import models

# Create your models here.
class View(models.Model):
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    age=models.IntegerField()
