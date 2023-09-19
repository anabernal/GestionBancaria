from django.shortcuts import render
from rest_framework.generics import ListAPIView
from aplicaciones.bancos.serialize import ciudadSerializer, clienteSerializer,cuentaBancariaSerializer,movimientoSerializer,operacionSerializer
from aplicaciones.bancos.models import Ciudad, Cliente, CuentaBancaria,Movimiento, Operacion
# Create your views here.


class listCiudadView(ListAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = ciudadSerializer

class listClienteView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer

class listCuentaBancariaView(ListAPIView):
    queryset = CuentaBancaria.objects.all()
    serializer_class = cuentaBancariaSerializer


class listMovimientoView(ListAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = movimientoSerializer

class listOperacionView(ListAPIView):
    queryset = Operacion.objects.all()
    serializer_class = operacionSerializer

