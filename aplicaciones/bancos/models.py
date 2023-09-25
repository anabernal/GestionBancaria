from django.db import models

# Create your models here.
class Ciudad (models.Model):
    nombre= models.CharField(max_length=100)
    departamento = models.CharField(max_length=30)
    codigoPostal = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.nombre} "

class Persona (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipoDocumento = models.CharField(max_length=100)
    nroDocumento = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    celular= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nroDocumento} - {self.nombre} {self.apellido}"

class Cliente (models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    fechaIngreso=models.DateTimeField()
    calificacion=models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.persona}"

class CuentaBancaria(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nroCuenta = models.CharField(max_length=100)
    fechaAlta=models.DateTimeField
    tipoCuenta = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    nroContrato = models.CharField(max_length=100)
    costoMantenimiento = models.DecimalField(max_digits=10, decimal_places=2)
    promedioAcreditacion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f" Nro de Cta:{self.nroCuenta} - Cliente:{self.cliente}"


class Movimiento(models.Model):
    cuenta=models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)
    fechaMovimiento=models.DateTimeField(auto_now_add=True)
    tipoMovimiento=models.CharField(max_length=30)
    saldoAnterior = models.DecimalField(max_digits=15,decimal_places=2)
    saldoActual = models.DecimalField(max_digits=15,decimal_places=2)
    montoMovimiento=models.DecimalField(max_digits=15,decimal_places=2)
    cuentaOrigen = models.IntegerField(default=0)
    cuentaDestino = models.IntegerField(default=0)
    canal = models.DecimalField(max_digits=15,decimal_places=2)











