from django.shortcuts import render, redirect

# Create your views here.
from .models import Reserva, Cliente, Hotel, Empleados, Habitacion
from hotelapp.forms import ReservaForms

# Create your views here.
def listar_reserva(request):
    reserva = Reserva.objects.all()
    return render(request, 'crm/reserva.html', {'reserva': reserva})

def listar_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'crm/cliente.html', {'cliente': cliente})

def listar_hotel(request):
    hotel = Hotel.objects.all()
    return render(request, 'crm/hotel.html', {'hotel': hotel})

def listar_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'crm/empleados.html', {'empleados': empleados})

def listar_habitacion(request):
    habitacion = Habitacion.objects.all()
    return render(request, 'crm/habitacion.html', {'habitacion': habitacion})

def registrarCliente(request):
    return render(request, 'crm/crear_clientes.html')

def AgregarCliente(request):
    a_nombre = request.POST['txt_nombre']
    a_direccion = request.POST['txt_direccion']
    a_rut = request.POST['txt_rut']
    a_celular = request.POST['txt_celular']
    a_correo = request.POST['txt_correo']

    crear = Cliente.objects.create(nombre = a_nombre, direccion = a_direccion, idcliente = a_rut, celular = a_celular, correo = a_correo)
    crear.save()
    return redirect('crear_reserva')

def crearReserva(request):
    if request.method == "POST":
        form = ReservaForms(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario_registro = "admin"
            reserva.save()
            return redirect('reserva')
    else:
        form = ReservaForms()
        context = {'form': form}
        return render(request, 'crm/crear_reserva.html', context)
