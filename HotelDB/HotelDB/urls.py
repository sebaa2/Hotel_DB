from django.contrib import admin
from django.urls import path, include
from CRM.views import listar_reserva, listar_cliente, listar_hotel, listar_empleados, listar_habitacion, AgregarCliente, registrarCliente, crearReserva, eliminar_reservar
#direcciones del login y registro
from CRM.views import principal, registro
from CRM.views import actualizar_reserva
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('lista-reserva/', listar_reserva, name="reserva"),
    path('lista-clientes/', listar_cliente, name="clientes"),
    path('lista-hotel/', listar_hotel, name="hotel"),
    path('lista-empleados/', listar_empleados, name="empleados"),
    path('lista-habitacion/', listar_habitacion, name="habitacion"),
    path('registrar-clientes/', registrarCliente, name="registar-cliente"),
    path('crear_reserva', crearReserva, name="crear_reserva"),
    path('eliminar_reserva/<int:idreserva>/', eliminar_reservar, name="eliminar_reserva"),
    path('agregarclientes/', AgregarCliente),


    #estas son las urls de pag principal y forms login
    path('', principal, name='principal'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
    path('editar-reserva/<int:idreserva>',actualizar_reserva,name="editar_reserva"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)