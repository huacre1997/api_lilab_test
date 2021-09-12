from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    puntuacion=models.CharField(max_length=20)
class Solicitud(models.Model):
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    aprobado=models.BooleanField(default=False)
    aprobado_por=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
