from django.db import models

class Iha (models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255,null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
  
