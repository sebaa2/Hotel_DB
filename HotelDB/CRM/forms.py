from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm


#esta clase es la del formulario de registro
class CustomUserCreationForm(UserCreationForm):
    pass
#fin de la logica de la clase

class ReservaForms(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [ 'estado_reserva', 'hotel_idhotel', 'cliente_idcliente']
        labels = {
            'estado_reserva' : 'Estado reserva: ',
            'hotel_idhotel' : 'Hotel: ',
            'cliente_idcliente' : 'Cliente: ',
        }
        widgets = {
            'estado_reserva' : forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_idhotel' : forms.Select(attrs={'class': 'form-control'}),
            'cliente_idcliente' : forms.Select(attrs={'class': 'form-control'})
        }
#agregar estos campos en models

