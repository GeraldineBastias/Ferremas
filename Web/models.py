from logging import PlaceHolder
from django.db import models

# Create your models here.

class RolUsuario(models.Model):
    idRol   = models.AutoField(primary_key=True)
    nomRol  = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomRol

class Usuario(models.Model):
    idUsuario        = models.AutoField(primary_key=True)
    nomUsuario       = models.CharField(max_length=50, blank=False, null=False)
    apellido         = models.CharField(max_length=50, blank=True, null=True)
    email            = models.CharField(max_length=50, null=False)
    contrasena       = models.CharField(max_length=30, null=False, blank=False)
    RolUsuario       = models.ForeignKey(RolUsuario, on_delete= models.CASCADE, default=1)

    def __str__(self) :
            return self.nomUsuario

class Producto(models.Model):
    idProducto    = models.AutoField(primary_key=True)
    nomProducto   = models.CharField(max_length=50, blank=False, null=False)
    foto          = models.ImageField(upload_to='foto_comida')
    descripcion   = models.CharField(max_length=1000, null=False, blank=False)
    costo         = models.IntegerField(null=False, blank=False)
    stock         = models.IntegerField(null=False, blank=False)

    def __str__(self) :
            return self.nomComida