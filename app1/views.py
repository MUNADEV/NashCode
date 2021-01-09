from django.shortcuts import render,HttpResponse 

# Create your views here.
def index(request):
    return render(request,"index.html")

def inicio_sesion(request):
    return render(request,"inicio_sesion.html")

def registro(request):
    return render(request,"registro.html")

def home(request):
    return render(request,"home.html")

def guardado(request):
    return render(request,"guardado.html")

def busqueda(request):
    return render(request,"busqueda.html")

def resultado_busqueda(request):
    return render(request,"resultado_busqueda.html")

def publicar(request):
    return render(request,"publicar.html") 

def editar(request):
    return render(request,"editar.html")

def publicacion(request):
    return render(request,"publicacion.html")

def perfil(request):
    return render(request,"perfil.html")

def miperfl(request):
    return render(request,"miperfil.html")

def editar_perfil(request):
    return render(request,"editar_perfil.html")