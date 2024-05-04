from django.shortcuts import render,redirect

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