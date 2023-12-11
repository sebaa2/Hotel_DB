# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
    def __str__(self):
        return f"{self.nombre}"


class Empleados(models.Model):
    idempleados = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    puesto = models.CharField(max_length=45, blank=True, null=True)
    salario = models.IntegerField(blank=True, null=True)
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
    def __str__(self):
        return f"{self.nombre}"

class Reserva(models.Model):
    idreserva = models.AutoField(primary_key=True)
    fecha_chekin = models.DateField(auto_now_add=True)
    fecha_chekout = models.DateField(blank=True, null=True)
    estado_reserva = models.CharField(max_length=45, blank=True, null=True)
    hotel_idhotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel_idhotel')
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_idcliente')

    class Meta:
        managed = False
        db_table = 'reserva'
