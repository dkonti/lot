from django.db import models

# Create your models here.

class Hashrate(models.Model):
    hash = models.FloatField(default=0.0000)