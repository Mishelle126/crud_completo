from django.db import models

# Create your models here.
class Casa(models.Model):
    cuarto = models.IntegerField()
    metro = models.IntegerField()
    baño = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    
