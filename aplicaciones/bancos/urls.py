from django.urls import path
from aplicaciones.bancos.views import listCiudadView, listClienteView, listCuentaBancariaView, listMovimientoView, listOperacionView
urlpatterns = [
    path('lista-ciudad/', listCiudadView.as_view()),
    path('lista-cliente/', listClienteView.as_view()),
    path('lista-operacion/', listCuentaBancariaView.as_view()),
    path('lista-movimiento/', listMovimientoView.as_view()),
    path('lista-cuenta/', listOperacionView.as_view()),

]