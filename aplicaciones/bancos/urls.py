from django.urls import path
from aplicaciones.bancos.views import *

urlpatterns = [
    # Objecto ciudad
    path('lista-ciudad/', listCiudadView.as_view()),
    path('buscar-ciudad/<kword>/', buscarCiudadView.as_view()),
    path('detalle-ciudad/<pk>/', detalleCiudadView.as_view()),
    path('registrar-ciudad/', registrarCiudadView.as_view()),
    path('modificar-ciudad/<pk>/', consultarAlterarCiudadView.as_view()),

    # Objecto persona
    path('lista-persona/', listPersonaView.as_view()),
    path('buscar-persona/<kword>/', buscarPersonaView.as_view()),
    path('detalle-persona/<pk>/', detallePersonaView.as_view()),
    path('registrar-persona/', registrarPersonaView.as_view()),
    path('modificar-persona/<pk>/', consultarAlterarPersonaView.as_view()),



# Objeto cliente
    path('lista-cliente/', listClienteView.as_view()),
    path('buscar-cliente/<kword>/', buscarClienteView.as_view()),
    path('detalle-cliente/<pk>/', detalleClienteView.as_view()),
    path('registrar-cliente/', registrarClienteView.as_view()),
    path('modificar-cliente/<pk>/', consultarAlterarClienteView.as_view()),


# Objeto CtaBancaria
    path('lista-ctabancaria/', listCtaBancariaView.as_view()),
    path('buscar-ctabancaria/<kword>/', buscarCtaBancariaView.as_view()),
    path('detalle-ctabancaria/<pk>/', detalleCtaBancariaView.as_view()),
    path('registrar-ctabancaria/', registrarCtaBancariaView.as_view()),
    path('modificar-ctabancaria/<pk>/', consultarAlterarCtaBancariaView.as_view()),


]