from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView, UpdateAPIView
from aplicaciones.bancos.serialize import ciudadSerializer,personaSerializer, clienteSerializer, ctaBancariaSerializer, movimientoSerializer
from aplicaciones.bancos.models import Ciudad,Persona, Cliente, CuentaBancaria, Movimiento
# Create your views here.

#Vistas relacionadas a Ciudad:
class listCiudadView(ListAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = ciudadSerializer

class buscarCiudadView(ListAPIView):
    serializer_class = ciudadSerializer
    def get_queryset(self):
        return Ciudad.objects.filter(
            nombre__icontains=self.kwargs['kword']
        )
class detalleCiudadView(RetrieveAPIView):
    serializer_class = ciudadSerializer
    queryset = Ciudad.objects.all()
class registrarCiudadView(CreateAPIView):
    serializer_class = ciudadSerializer
class consultarAlterarCiudadView(RetrieveUpdateDestroyAPIView):
    serializer_class = ciudadSerializer
    queryset = Ciudad.objects.all()
# Vistas relacionadas a Movimiento



##################################################################################################################
#Vistas relacionadas a Persona

class listPersonaView(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = personaSerializer

class buscarPersonaView(ListAPIView):
    serializer_class = personaSerializer
    def get_queryset(self):
        return Persona.objects.filter(
            nombre__icontains=self.kwargs['kword']
        )

class detallePersonaView(RetrieveAPIView):
    serializer_class = personaSerializer
    queryset = Persona.objects.all()
class registrarPersonaView(CreateAPIView):
    serializer_class = personaSerializer
class consultarAlterarPersonaView(RetrieveUpdateDestroyAPIView):
    serializer_class = personaSerializer
    queryset = Persona.objects.all()



# Vistas relacionadas a Cliente

class listClienteView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer

class buscarClienteView(ListAPIView):
    serializer_class = clienteSerializer
    def get_queryset(self):
        return Cliente.objects.filter(
            nombre__icontains=self.kwargs['kword']
        )
class detalleClienteView(RetrieveAPIView):
    serializer_class = clienteSerializer
    queryset = Cliente.objects.all()
class registrarClienteView(CreateAPIView):
    serializer_class = clienteSerializer
class consultarAlterarClienteView(RetrieveUpdateDestroyAPIView):
    serializer_class = clienteSerializer
    queryset = Cliente.objects.all()


# Vistas relacionadas a Cta Bancaria
class listCtaBancariaView(ListAPIView):
    queryset = CuentaBancaria.objects.all()
    serializer_class = ctaBancariaSerializer

class buscarCtaBancariaView(ListAPIView):
    serializer_class = ctaBancariaSerializer
    def get_queryset(self):
        return CuentaBancaria.objects.filter(
            nroCuenta__icontains=self.kwargs['kword']
        )
class detalleCtaBancariaView(RetrieveAPIView):
    serializer_class = ctaBancariaSerializer
    queryset = CuentaBancaria.objects.all()
class registrarCtaBancariaView(CreateAPIView):
    serializer_class = ctaBancariaSerializer
class consultarAlterarCtaBancariaView(RetrieveUpdateDestroyAPIView):
    serializer_class = ctaBancariaSerializer
    queryset = CuentaBancaria.objects.all()




# Vistas relacionadas a Movimiento
class listMovimientoView(ListAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = movimientoSerializer

class buscarMovimientoView(ListAPIView):
    serializer_class = movimientoSerializer
    def get_queryset(self):
        return Movimiento.objects.filter(
            ctaOrigen__icontains=self.kwargs['kword']
        )
class detalleMovimientoView(RetrieveAPIView):
    serializer_class = movimientoSerializer
    queryset = Movimiento.objects.all()
class registrarMovimientoView(CreateAPIView):
    serializer_class = movimientoSerializer
class consultarAlterarMovimientoView(RetrieveUpdateDestroyAPIView):
    serializer_class = movimientoSerializer
    queryset = Movimiento.objects.all()


