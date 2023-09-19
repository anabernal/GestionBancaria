from django.db import models

# Create your models here.
class Ciudad (models.Model):
    nombre= models.CharField(max_length=100)

class Cliente (models.Model):
    nombre= models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)

class CuentaBancaria(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    propietario=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    bloqueada=models.BooleanField(default=False)

class Movimiento(models.Model):
    cuenta=models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)
    tipo=models.CharField(max_length=10)
    monto=models.DecimalField(max_digits=10,decimal_places=2)

class Operacion(models.Model):
    nombre=models.CharField(max_length=100)

