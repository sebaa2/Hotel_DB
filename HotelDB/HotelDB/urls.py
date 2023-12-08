from django.contrib import admin
from django.urls import path, include
from CRM.views import listar_reserva, listar_cliente, listar_hotel, listar_empleados, listar_habitacion, AgregarCliente, logout, registrarCliente, crearReserva, login_view, login_
#direcciones del login y registro
from reservas.views import principal, registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista-reserva/', listar_reserva, name="reserva"),
    path('lista-clientes/', listar_cliente, name="clientes"),
    path('lista-hotel/', listar_hotel, name="hotel"),
    path('lista-empleados/', listar_empleados, name="empleados"),
    path('lista-habitacion/', listar_habitacion, name="habitacion"),
    path('registrar-clientes/', registrarCliente, name="registar-cliente"),
    path('crear_reserva', crearReserva, name="crear_reserva"),
    path('agregarclientes/', AgregarCliente),
    path('login/',login_view, name="login"),
    path('logout/',logout, name="logout"),
    #estas son las urls de pag principal y forms login
    path('', principal, name='principal'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
]
