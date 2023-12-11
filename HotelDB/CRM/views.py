from django.shortcuts import get_object_or_404, render, redirect

from .models import Reserva, Cliente, Hotel, Empleados, Habitacion
from CRM.forms import ReservaForms
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

#redirrecion a la pagina principal
def principal(request):
    return render(request, 'crm/principal.html')

#creacion de la cuenta para el login
def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect("principal")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#inicio de las clases que recopilan los datos de la base de datos
def listar_reserva(request):
    #if para verificar si el usuario esta logeado
    reserva = Reserva.objects.all()
    return render(request, 'crm/reserva.html', {'reserva': reserva})

def listar_cliente(request):
    #if para verificar si el usuario esta logeado
    cliente = Cliente.objects.all()
    return render(request, 'crm/cliente.html', {'cliente': cliente})

def listar_hotel(request):
    #if para verificar si el usuario esta logeado
    hotel = Hotel.objects.all()
    return render(request, 'crm/hotel.html', {'hotel': hotel})

def listar_empleados(request):
    #if para verificar si el usuario esta logeado

    empleados = Empleados.objects.all()
    return render(request, 'crm/empleados.html', {'empleados': empleados})

def listar_habitacion(request):
    #if para verificar si el usuario esta logeado
    habitacion = Habitacion.objects.all()
    return render(request, 'crm/habitacion.html', {'habitacion': habitacion})
#fin de las clases que recopilan los datos de la base de datos


#clase dedicada a la creacion de clientes
def registrarCliente(request):
    return render(request, 'crm/crear_clientes.html')

def AgregarCliente(request):
    #if para verificar si el usuario esta logeado

    a_nombre = request.POST['txt_nombre']
    a_direccion = request.POST['txt_direccion']
    a_rut = request.POST['txt_rut']
    a_celular = request.POST['txt_celular']
    a_correo = request.POST['txt_correo']

    crear = Cliente.objects.create(nombre = a_nombre, direccion = a_direccion, idcliente = a_rut, celular = a_celular, correo = a_correo)
    crear.save()
    return redirect('crear_reserva')

def crearReserva(request):
    #if para verificar si el usuario esta logeado
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

def editarReserva(request, idreserva):
    #if para verificar si el usuario esta logeado
    reserva = get_object_or_404(Reserva, pk = idreserva)
    if request.method == 'POST':
        form = ReservaForms(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
        return redirect('reserva')
    else:
        form = ReservaForms(instance=reserva)
        context = {'form': form, 'reserva': reserva}

    return render(request, 'crm/editar_reserva.html',context)

#login para los empleados del hotel
#no borrar aun


#clase dedicada a la actualizacion de las reservas del hotel
from django.http import HttpResponseNotFound
def actualizar_reserva(request, idreserva):
    reserva = get_object_or_404(Reserva, pk = idreserva)
    if request.method =="POST":
        form = ReservaForms(request.POST, instance = reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva')
    else:
        form = ReservaForms(instance = reserva)
    context = {'form' : form,'reserva' : reserva}
    return render(request,'crm/actualizar_reserva.html',context)

def eliminar_reservar(request, idreserva):
    try:
        # Obtiene la reserva a eliminar
        reserva = Reserva.objects.get(idreserva=idreserva)
        # Elimina la reserva
        reserva.delete()  
        # Redirecciona a la lista de reservas
        return redirect('reserva')
    except Reserva.DoesNotExist:
        # Retorna un error 404 en caso de no encontrar la reserva
        return HttpResponseNotFound('Reserva no encontrada')
from django.http import HttpResponseNotFound
