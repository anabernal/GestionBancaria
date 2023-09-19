from  rest_framework import serializers
from aplicaciones.bancos.models import Ciudad,Cliente,CuentaBancaria,Operacion,Movimiento


class ciudadSerializer(serializers.ModelSerializer):

    class Meta:
        model= Ciudad
        fields=('__all__')

class clienteSerializer(serializers.ModelSerializer):

    class Meta:
        model= Cliente
        fields=('__all__')

class operacionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Operacion
        fields=('__all__')

class cuentaBancariaSerializer(serializers.ModelSerializer):

    class Meta:
        model= CuentaBancaria
        fields=('__all__')

class movimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Movimiento
        fields=('__all__')
