from django.db import models

# Create your models here.
class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Empleados(models.Model):
    idempleados = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    puesto = models.CharField(max_length=45, blank=True, null=True)
    hotel_idhotel = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='hotel_idhotel')

    class Meta:
        managed = False
        db_table = 'empleados'


class Habitacion(models.Model):
    idhabitacion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    hotel_idhotel = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='hotel_idhotel')

    class Meta:
        managed = False
        db_table = 'habitacion'


class Hotel(models.Model):
    idhotel = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class Reserva(models.Model):
    idreserva = models.AutoField(primary_key=True)
    fecha_chekin = models.DateField(blank=True, null=True)
    fecha_chekout = models.DateField(blank=True, null=True)
    estado_reserva = models.CharField(max_length=45, blank=True, null=True)
    hotel_idhotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel_idhotel')
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_idcliente')

    class Meta:
        managed = False
        db_table = 'reserva'
