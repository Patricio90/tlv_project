from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut=models.CharField(max_length=10, unique=True, default='None')
    nombre=models.CharField(max_length=50, default='None')
    apellido=models.CharField(max_length=100, default='None')
    correo=models.CharField(max_length=50, default='None')
    telefono=models.IntegerField()
