from django.db import models

# Create your models here.

class url(models.Model):
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)
