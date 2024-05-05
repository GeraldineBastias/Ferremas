from unicodedata import name
from django.urls import URLPattern, path
from . import views
from .views import  loginUsuario,webpay,payment,PagoCorrecto,transaccioncompleta,modificarContra,modificarUsuario,registrarUsuario,fotoUsuarioModificada,index,about, contact, destornilla_1,destornilla_2, martillo_1,martillo_2, martillos, pintura_1,pintura_2,pinturas, shop,destornilladores,login
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

     #Con sesion
    path('index/<str:sesion>',index,name="index"),
    path('about/<str:sesion>',about,name="about"),
    path('contact/<str:sesion>',contact,name="contact"),
    path('destornilla_1/<str:sesion>',destornilla_1,name="destornilla_1"),
    path('destornilla_2/<str:sesion>',destornilla_2,name="destornilla_2"),
    path('destornilladores/<str:sesion>',destornilladores,name="destornilladores"),
    path('martillo_1/<str:sesion>',martillo_1,name="martillo_1"),
    path('martillo_2/<str:sesion>',martillo_2,name="martillo_2"),
    path('martillos/<str:sesion>',martillos,name="martillos"),
    path('pintura_1/<str:sesion>',pintura_1,name="pintura_1"),
    path('pintura_2/<str:sesion>',pintura_2,name="pintura_2"),
    path('pinturas/<str:sesion>',pinturas,name="pinturas"),
    path('shop/<str:sesion>',shop,name="shop"),

    #Sin sesion
    path('',login,name="login"),
    path('loginUsuario',loginUsuario,name="loginUsuario"),
    #Funciones
    path('fotoUsuarioModificada/<str:sesion>',fotoUsuarioModificada,name="fotoUsuarioModificada"),
    path('registrarUsuario',registrarUsuario,name="registrarUsuario"),
    path('modificarUsuario/<str:sesion>/<int:id>',modificarUsuario,name="modificarUsuario"),
    path('modificarContra/<str:sesion>/<int:id>',modificarContra,name="modificarContra"),

    #Transbank
    path('transaccioncompleta/<str:sesion>/<str:idcar>/', transaccioncompleta, name='transaccioncompleta'),
    path('PagoCorrecto/', PagoCorrecto, name='PagoCorrecto'),
    path('payment/', payment, name='payment'),
    path('webpay/<str:sesion>/<int:monto>/<int:idcar>', webpay, name='webpay'),


]










