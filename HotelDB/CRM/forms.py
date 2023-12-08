from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm


#esta clase es la del formulario de registro
class CustomUserCreationForm(UserCreationForm):
    pass
#hasta aqui gg    

class ReservaForms(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [ 'fecha_chekin', 'fecha_chekout', 'estado_reserva', 'hotel_idhotel', 'cliente_idcliente']
        labels = {
            'fecha_chekin' : 'Fecha registrarse: ',
            'fecha_chekout' : 'Fecha chekout: ',
            'estado_reserva' : 'Estado reserva: ',
            'hotel_idhotel' : 'Hotel: ',
            'cliente_idcliente' : 'Cliente: ',
        }
        widgets = {
            'fecha_chekin' : forms.TimeInput(attrs={'class': 'form-control'}),
            'fecha_chekout' : forms.TimeInput(attrs={'class': 'form-control'}),
            'estado_reserva' : forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_idhotel' : forms.Select(attrs={'class': 'form-control'}),
            'cliente_idcliente' : forms.Select(attrs={'class': 'form-control'})
        }
#agregar estos campos en models
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
