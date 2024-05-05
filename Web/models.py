from django.db import models

# Create your models here.

class Tipo_Usuario(models.Model):
    id_tipo_user = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self) :
            return self.descripcion

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    foto = models.ImageField(upload_to="foto_perfil", default="../../static/core/img/defaultuser.png", blank='')
    id_tipo_user = models.ForeignKey(Tipo_Usuario, on_delete= models.CASCADE, default=1)

    def __str__(self) :
            return self.email

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, null=False, blank=False)
    imagen = models.ImageField(upload_to="foto_producto", default="../../static/core/img/defaultuser.png", blank='')

    def __str__(self) :
            return self.descripcion
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=60, null=False, blank=False)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    marca = models.CharField(max_length=60, null=False, blank=False)
    valor = models.IntegerField(null=False, blank=False)
    imagen = models.ImageField(upload_to="foto_producto", default="../../static/core/img/defaultuser.png", blank='')
    id_Categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self) :
            return self.nombre

class Carrito(models.Model): 
    id_carrito = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(null=False, blank=False)
    id_user = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
   

class Boleta(models.Model): 
    num_boleta = models.AutoField(primary_key=True)
    emision = models.DateField(null=False, blank=False)
    neto = models.IntegerField(null=False, blank=False)
    iva = models.IntegerField(null=False, blank=False)
    total = models.IntegerField(null=False, blank=False)
    id_user = models.ForeignKey(Usuario, on_delete= models.CASCADE)

class Producto_Comprado(models.Model): 
    id_producto_comprado = models.AutoField(primary_key=True)
    id_serie = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    valor_final = models.IntegerField(null=False, blank=False)
    num_boleta = models.ForeignKey(Boleta, on_delete= models.CASCADE)




