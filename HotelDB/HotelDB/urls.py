"""
URL configuration for HotelDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRM.views import listar_reserva, listar_cliente, listar_hotel, listar_empleados, listar_habitacion, AgregarCliente, logout, registrarCliente, crearReserva, login_view, login_


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
]
