from django.shortcuts import render,HttpResponse,redirect
from .models import Usuario, Publicacion

# Create your views here.
class Usuario_actual:
	id = 0
	logeado = False

usuario_actual = Usuario_actual()

def index(request):
    usuario_actual.logeado = False
    return render(request,"index.html")

def inicio_sesion(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if Usuario.objects.filter(email = email,password=password).exists():
            usuario = Usuario.objects.get(email = email)
            usuario_actual.id = usuario.id_usuario
            usuario_actual.logeado = True

            return redirect("/nashcode.com/home")

    return render(request,"inicio_sesion.html")

def registro(request):
    if request.method == "POST":
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
        usuario_actual.id = nuevo_usuario.id_usuario
        usuario_actual.logeado = True

        return redirect("/nashcode.com/home")

    return render(request,"registro.html")

def home(request):
    if usuario_actual.logeado == False:
        return redirect("/nashcode.com")

    usuario = Usuario.objects.get(id_usuario = usuario_actual.id)
    publicacion_list = Publicacion.objects.all()
    populares = Publicacion.objects.order_by('likes').reverse()[:3]
    
    contexto = {
        "usuario" : usuario,
        "publicacion_list" : publicacion_list,
        "populares" : populares
    }
    return render(request,"home.html",contexto)

def guardado(request):
    return render(request,"guardado.html")

def busqueda(request):

    return render(request,"busqueda.html")

def resultado_busqueda(request):
    if usuario_actual.logeado == False:
       return redirect("/nashcode.com")

    if request.method == "POST":
        titulo = request.POST["titulo"]
        categoria = request.POST["categoria"]
        publicacion_list = Publicacion.objects.filter(titulo__contains=titulo,categoria__contains=categoria)

        contexto = {
            "titulo" : titulo,
            "categoria" : categoria,
            "publicacion_list" : publicacion_list
        }
        return render(request,"resultado_busqueda.html",contexto)
    return redirect("/nashcode.com/busqueda")

def publicar(request):
    if usuario_actual.logeado == False:
       return redirect("/nashcode.com")

    if request.method == "POST":

        usuario = Usuario.objects.get(id_usuario = usuario_actual.id)
        titulo = request.POST["titulo"]
        codigo = request.POST["codigo"]
        descripcion = request.POST["descripcion"]
        categoria = request.POST["categoria"]
    
        nueva_publicacion = Publicacion()
        nueva_publicacion.usuario = usuario
        nueva_publicacion.titulo = titulo
        nueva_publicacion.codigo = codigo
        nueva_publicacion.descripcion = descripcion
        nueva_publicacion.categoria = categoria
        nueva_publicacion.likes = 0
        nueva_publicacion.save()
        return redirect("/nashcode.com/home")

    return render(request,"publicar.html")

def editar(request,id):
    if usuario_actual.logeado == False:
       return redirect("/nashcode.com")

    if request.method == "POST":

        titulo = request.POST["titulo"]
        codigo = request.POST["codigo"]
        descripcion = request.POST["descripcion"]
        categoria = request.POST["categoria"]

        actualizar_publicacion = Publicacion.objects.get(id_publicacion = id)
        actualizar_publicacion.titulo = titulo
        actualizar_publicacion.codigo = codigo
        actualizar_publicacion.descripcion = descripcion
        actualizar_publicacion.categoria = categoria
        actualizar_publicacion.save()
        return redirect("/nashcode.com/home")

    publicacion = Publicacion.objects.get(id_publicacion = id)
    
    contexto = {
        "publicacion" : publicacion
    }
    return render(request,"editar.html",contexto)

def publicacion(request,id):
    if usuario_actual.logeado == False:
        return redirect("/nashcode.com")

    publicacion = Publicacion.objects.get(id_publicacion = id)
    usuario = Usuario.objects.get(id_usuario = usuario_actual.id)

    contexto = {
        "publicacion" : publicacion,
        "usuario" : usuario
    }
    return render(request,"publicacion.html",contexto)

def perfil(request,id):
    if usuario_actual.logeado == False:
        return redirect("/nashcode.com")

    perfil_usuario = Usuario.objects.get(id_usuario = id)
    usuario = Usuario.objects.get(id_usuario = usuario_actual.id)

    contexto = {
        "perfil_usuario" : perfil_usuario,
        "usuario" : usuario
    }
    return render(request,"perfil.html",contexto)

def editar_perfil(request):
    if usuario_actual.logeado == False:
        return redirect("/nashcode.com")

    if request.method == "POST":
        nombre = request.POST["nombre"]
        alias = request.POST["alias"]
        email = request.POST["email"]

        actualizar_usuario = Usuario.objects.get(id_usuario = usuario_actual.id)
        actualizar_usuario.nombre = nombre
        actualizar_usuario.alias = alias
        actualizar_usuario.email = email
        actualizar_usuario.save()
        return redirect("/nashcode.com/home")

    usuario = Usuario.objects.get(id_usuario = usuario_actual.id)
    contexto = {
        "usuario" : usuario
    }
    return render(request,"editar_perfil.html",contexto)