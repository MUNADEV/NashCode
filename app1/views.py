from django.shortcuts import HttpResponse, redirect, render 
from .models import Usuario, Publicacion
from django.http import request
# Create your views here.
def index(request):
    return render(request,"index.html")

def inicio_sesion(request):
    return render(request,"inicio_sesion.html")

def registro(request):
    
    if request.method == "POST":
        print("POST")
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
        nuevo_usuario.save()
       
        return redirect("/nashcode.com")
  
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
   
    if request.method == "POST":
        #usuario = 1 #AQUI SE OCUPA USUARIO nombre
        usuario = "hola"
        titulo = request.POST["titulo"]
        codigo = request.POST["codigo"]
        descripcion = request.POST["descripcion"]
        categoria = request.POST["lenguaje"]
    
        nueva_publicacion = Publicacion()
        #nueva_publicacion.usuario = usuario
        nueva_publicacion.usuario = usuario
        nueva_publicacion.titulo = titulo
        nueva_publicacion.codigo = codigo
        nueva_publicacion.descripcion = descripcion
        nueva_publicacion.categoria = categoria
        nueva_publicacion.likes = 0
        nueva_publicacion.save()

        return redirect("/nashcode.com/home")

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