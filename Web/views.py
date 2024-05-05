from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario, Tipo_Usuario, Categoria,Producto,Carrito
from django.contrib import messages
import base64
from random import randint
import transbank
from transbank.webpay.webpay_plus.transaction import Transaction

# Create your views here.

#------------------------API DE WEBPAY-------------------------------

def webpay(request,sesion,monto,idcar):

    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    y = Carrito.objects.get(id_carrito = idcar)

    Monto = monto * y.cantidad
    #crea la transaccion
    idcarstr = str(idcar)
    resp = (Transaction()).create(str(randint(10,100000)), str(randint(10,100000)), float(Monto), "http://localhost:8000/transaccioncompleta/"+sesion+"/"+idcarstr)

    contexto = {
        "sesion":sesion,
        "usuario":x,
        "token":resp['token'],
        "url":resp['url'],
        "carrito":y
    }
    #redirige a confirmar pago donde evia el monto a pagar tambien la url y el token devuelto por parte de transbank
    return render(request, "core/a_VistaCliente/payment.html",contexto)

#-----------------------------------------------------------------------------

def transaccioncompleta(request,sesion,idcar):
    token = request.GET.get('token_ws')
    y = Carrito.objects.get(id_carrito = idcar)
    if token:
        transaction = Transaction()
        response = transaction.commit(token=token)

        amount= response['amount']
        status = response['status']
        buy_order= response['buy_order']
        transaction_date = response['transaction_date']
        authorization_code = response['authorization_code']

        contexto = {
        'amount':amount,
        'status':status,
        'buy_order':buy_order,
        'transaction_date':transaction_date,
        'authorization_code':authorization_code,
        'sesion':sesion,
        'carrito':y
    }
    return render(request, "core/a_VistaCliente/PagoCorrecto.html",contexto)

#-----------------------------------------------------------------------------

def PagoCorrecto(request):
    
    return render(request, 'core/a_VistaCliente/PagoCorrecto.html')

#-----------------------------------------------------------------------------

def payment(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request, 'core/payment.html',contexto)

#-----------------------------------------------------------------------------

def login(request):
    return render(request,'Web/login.html')

def index(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/index.html',contexto)

def contact(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/contact.html',contexto)

def destornilla_1(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/destornilla_1.html',contexto)

def destornilla_2(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/destornilla_2.html',contexto)

def destornilladores(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/destornilladores.html',contexto)

def martillo_1(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/martillo_1.html',contexto)

def martillo_2(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/martillo_2.html',contexto)

def martillos(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/martillos.html',contexto)

def pintura_1(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/pintura_1.html',contexto)

def pintura_2(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/pintura_2.html',contexto)

def pinturas(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/pinturas.html',contexto)

def shop(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/shop.html',contexto)

def about(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    return render(request,'Web/about.html',contexto)

#------------- FUNCIONES LOGIN Y DEMÁS ----------------

#-----------------------------------------------------------------------------
def registrarUsuario(request):
    nombre2     = request.POST['nomUser']
    apellido2   = request.POST['apeUser']
    email2      = request.POST['email']
    contra2     = request.POST['password1']

    try:
        c = Usuario.objects.get(email = email2)
        c1 = False
    except Usuario.DoesNotExist:
        c1 = True      
    
    if c1 == True:
        Usuario.objects.create(nomUsuario = nombre2, apellido = apellido2, email = email2, contrasena = contra2)

        sesion = Usuario.objects.get(nomUsuario=nombre2)
        contexto ={
        "sesion":sesion
        }
        messages.success(request, 'Cuenta registrada')
        return render(request,"Web/index.html",contexto)
    else:
        messages.error(request, 'El correo ya esta ocupado')
        return redirect ('Registrarse')
    
#-----------------------------------------------------------------------------
def listadoUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {"lista_u":usuario}
    return render(request,"Web/Listar_Usuario.html", contexto)


#-----------------------------------------------------------------------------
def Listar_Usuario(request):
    UserAdmin = Usuario.objects.all()
    contexto = {
        "usuario":UserAdmin,
        }
    return render(request,'Web/Listar_Usuario.html',contexto)
#-----------------------------------------------------------------------------


#--------------------CARRITO DE COMPRA------------------------------------

def carrito(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    carrito = Carrito.objects.all()
    contexto = {
        "sesion":sesion,
        "usuario":x,
        "lista_v":carrito
    }
    return render(request, 'core/a_VistaCliente/carrito.html',contexto)

#-----------------------------------------------------------------------------

def agregarCarrito(request,sesion,serie):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    y = Serie.objects.get(id_serie = serie)
    cantidad1     = request.POST['cantidad']
    cantidad2     = request.POST['divStoc']

    if cantidad1 <= cantidad2:
        try:
            Carrito.objects.get(id_serie=y, id_user =x)
            return redirect('detalleProducto',sesion,serie)
        except:
            canti = cantidad1

            Carrito.objects.create(
            cantidad = canti,       
            id_user = x,
            id_serie =  y
            )
            return redirect('carrito',sesion)
    else:
        return redirect('detalleProducto',sesion,serie)
    
#-----------------------------------------------------------------------------

def eliminarCarrito(request,sesion,id):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    carrito = Carrito.objects.get(id_carrito = id)
    carrito.delete() #Elimina registro
    contexto = {
        "sesion":sesion,
        "usuario":x,
    }
    return redirect('carrito',sesion)

#-----------------------------------------------------------------------------

def eliminarproducto(request,sesion,id):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    producto = Producto.objects.get(id_producto = id)
    producto.delete() #Elimina registro
    return redirect('gestionCategoria',sesion)

#-----------------------------------------------------------------------------

def registrarProducto(request,sesion):
    codigo1              = request.POST['codigo']
    nombre1              = request.POST['nombre']
    marca1               = request.POST['marca']
    valor1               = request.POST['valor']
    id_categoria1        = request.POST['id_categoria']

    id_categoria2 = Categoria.objects.get(id_categoria = id_categoria1)
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    try:
        imagen1          = request.FILES['imagen']
        Producto.objects.create(
            codigo = codigo1,       
            nombre = nombre1,
            marca = marca1,
            valor = valor1,
            id_categoria = id_categoria2,
            imagen = imagen1   
        )
        return redirect('gestionProducto',sesion)
    except:
        Producto.objects.create(
            codigo = codigo1,       
            nombre = nombre1,
            marca = marca1,
            valor = valor1,
            id_tipo_producto = id_categoria2    
        )
        return redirect('gestionProducto',sesion)

#-----------------------------------------------------------------------------

def registrarTipoProducto(request,sesion):
    desc1     = request.POST['desc']
    id_cat    = request.POST['id_cat']
    categoria = Categoria.objects.get(id_categoria = id_cat)
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
       
    try:
        imagen1          = request.FILES['imagen']
        Categoria.objects.create(
            descripcion=desc1,
            id_categoria = categoria,
            imagen = imagen1
        )
        return redirect('gestionTipoProducto',sesion)
    except:
        Categoria.objects.create(
            descripcion=desc1,
            id_categoria = categoria
        )
        return redirect('gestionTipoProducto',sesion)

#-----------------------------------------------------------------------------

def eliminarTipoProducto(request,sesion,id):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    tipoProducto = Categoria.objects.get(id_categoria = id)
    tipoProducto.delete() #Elimina registro
    return redirect('gestionTipoProducto',sesion)

#-----------------------------------------------------------------------------

def gestionStock(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    producto = Producto.objects.all()
    categoria = Categoria.objects.all()
    contexto = {
        "sesion":sesion,
        "usuario":x,
        "Categoria":categoria
    }
    return render(request, 'core/gestiones/gestionStock.html',contexto)

#-----------------------------------------------------------------------------


#-----------------------FUNCIONES APARTE------------------------------------

def fotoUsuarioModificada(request,sesion):
    base64_string = sesion
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    x = Usuario.objects.get(email = sample_string)
    contexto = {
        "sesion":sesion,
        "usuario":x
    }
    
    usuario = Usuario.objects.get(email = sample_string)
    foto2 = request.FILES['fot']
      
    usuario.foto = foto2
    usuario.save() #update
    
    return redirect ('modificarFotoPerfil',sesion)

#-----------------------------------------------------------------------------

def modificarContra(request,sesion,id):
    password1  = request.POST['passw']
    
    usuario = Usuario.objects.get(id_user=id)
    
    usuario.password = password1
    usuario.save() #update
    return redirect('perfil',sesion)

#-----------------------------------------------------------------------------

def modificarUsuario(request,sesion,id):
    # password1       = request.POST['passw']
    nombre1         = request.POST['nom']

    
    usuario = Usuario.objects.get(id_user=id)
    
    usuario.nombre = nombre1

    usuario.save() #update
    return redirect('perfil',sesion)

#-----------------------------------------------------------------------------

def loginUsuario(request):
    co = request.POST['corre']
    ps = request.POST['pass']
    
    try:
        user = Usuario.objects.get(email = co, password = ps)
        sample_string = co
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        sesion = base64_string

   
        return redirect ('home',sesion)
 
    except Usuario.DoesNotExist:
        return redirect ('login')

#-----------------------------------------------------------------------------

def registrarUsuario(request):
    email1          = request.POST['correo']
    password1       = request.POST['passw']
    nombre1         = request.POST['nom']

    try:
        c = Usuario.objects.get(email = email1)
        c1 = False
    except Usuario.DoesNotExist:
        c1 = True      


    if c1 == True:
      
        Usuario.objects.create(
            email = email1,
            password = password1,
            nombre = nombre1,)

        #messages.success(request, 'Cuenta registrada')
        return redirect('login')
    else:
        #messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        return redirect('login')


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------



















