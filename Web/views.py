from email import message
from django.shortcuts import render, redirect
from .models import Usuario, RolUsuario, Producto
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'Web/index.html')

def contact(request):
    return render(request,'Web/contact.html')

def destornilla_1(request):
    return render(request,'Web/destornilla_1.html')

def destornilla_2(request):
    return render(request,'Web/destornilla_2.html')

def destornilladores(request):
    return render(request,'Web/destornilladores.html')

def martillo_1(request):
    return render(request,'Web/martillo_1.html')

def martillo_2(request):
    return render(request,'Web/martillo_2.html')

def martillos(request):
    return render(request,'Web/martillos.html')

def pintura_1(request):
    return render(request,'Web/pintura_1.html')

def pintura_2(request):
    return render(request,'Web/pintura_2.html')

def pinturas(request):
    return render(request,'Web/pinturas.html')

def shop(request):
    return render(request,'Web/shop.html')

def about(request):
    return render(request,'Web/about.html')

#------------- FUNCIONES LOGIN Y DEMÁS ----------------
def login_app(request):
    us = request.POST['nomUser']
    cl = request.POST['pass']
    try:
        if us == 'admin' and cl == 'admin':
            return redirect ('Vista_Admin')
        elif us == 'usuario' and cl == 'usuario':
            return redirect ('Vista_Usuario')
        else:
            return redirect ('index')

    except Usuario.DoesNotExist:
        # messages.error(request, 'Usuario y/o clave incorrecta')
        return redirect ('index')
    

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




























