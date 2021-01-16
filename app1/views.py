from django.shortcuts import render,HttpResponse,redirect
from .models import Usuario, Publicacion

# Create your views here.
def index(request):
    return render(request,"index.html")

def inicio_sesion(request):
    return render(request,"inicio_sesion.html")

def registro(request):
    if request.method == "POST":
        print("entre por post")
        nombre = request.POST["nombre"]
        alias = request.POST["alias"]
        email = request.POST["email"]
        password = request.POST["password"]

        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = nombre
        nuevo_usuario.alias = alias
        nuevo_usuario.email = email
        nuevo_usuario.password = password
        nuevo_usuario.likes = 0
        #nuevo_usuario.save()
        return redirect("/nashcode.com/home")

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

def mi_perfil(request):
    return render(request,"mi_perfil.html")

def editar_perfil(request):
    return render(request,"editar_perfil.html")