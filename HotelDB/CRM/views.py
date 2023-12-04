from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseNotFound
from .models import Reserva, Cliente, Hotel, Empleados, Habitacion
from CRM.forms import LoginForm, ReservaForms

# Create your views here.
def listar_reserva(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

    reserva = Reserva.objects.all()
    return render(request, 'crm/reserva.html', {'reserva': reserva})

def listar_cliente(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

    cliente = Cliente.objects.all()
    return render(request, 'crm/cliente.html', {'cliente': cliente})

def listar_hotel(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

    hotel = Hotel.objects.all()
    return render(request, 'crm/hotel.html', {'hotel': hotel})

def listar_empleados(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

    empleados = Empleados.objects.all()
    return render(request, 'crm/empleados.html', {'empleados': empleados})

def listar_habitacion(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

    habitacion = Habitacion.objects.all()
    return render(request, 'crm/habitacion.html', {'habitacion': habitacion})

def registrarCliente(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

    return render(request, 'crm/crear_clientes.html')

def AgregarCliente(request):
    #if para verificar si el usuario esta logeado
    if not request.session.get('autenticado'):
        return redirect('login')

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
    if not request.session.get('autenticado'):
        return redirect('login')

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
    if not request.session.get('autenticado'):
        return redirect('login')

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
def login_view(request):
    form = LoginForm(request.POST)
    #python.exe \manage.py migrate sessions (para el login)
    #agregar los campos al models para que funcione, en el de empleados
    if request.method == 'POST'and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #esta seccion del codigo necesitara modificacion para u funcionamiento
        try:
            user = Empleados.objects.get(nombre=username)
            if user.password == password:
                request.session['autenticado'] = True
                request.session['usuario'] = user.nombre #esta linea es la que se debe modificar
                request.session['nombre_completo'] = user.nombre + ' ' #depende de que uso le daremos
                return redirect("empleados")
            else:
                form.add_error(None, "Contraseña incorrecta")
        except Empleados.DoesNotExist:
            form.add_error(None, "Usuario incorrecto")
    return render(request, 'crm/login.html', {'form': form})