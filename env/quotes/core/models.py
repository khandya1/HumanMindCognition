from django.db import models
  
# Create your models here.
  
  
class React(models.Model):
    name = models.CharField(max_length=300)
    detail = models.CharField(max_length=500)