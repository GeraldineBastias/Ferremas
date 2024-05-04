from unicodedata import name
from django.urls import URLPattern, path
from . import views
from .views import  index,about, contact, destornilla_1,destornilla_2, martillo_1,martillo_2, martillos, pintura_1,pintura_2,pinturas, shop
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',index,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('destornilla_1',destornilla_1,name="destornilla_1"),
    path('destornilla_2',destornilla_2,name="destornilla_2"),
    path('martillo_1',martillo_1,name="martillo_1"),
    path('martillo_2',martillo_2,name="martillo_2"),
    path('martillos',martillos,name="martillos"),
    path('pintura_1',pintura_1,name="pintura_1"),
    path('pintura_2',pintura_2,name="pintura_2"),
    path('pinturas',pinturas,name="pinturas"),
    path('shop',shop,name="shop"),


]










