from django.urls import path,include
from . import views

urlpatterns = [
    path('nashcode.com',views.index),
    path('nashcode.com/iniciosesion',views.inicio_sesion),
    path('nashcode.com/registro',views.registro),
    
    #path('nashcode.com/<string : username>/home',views.home),
    #path('nashcode.com/<string : username>/guardado',views.guardado),
    #path('nashcode.com/<string : username>/busqueda',views.busqueda),
    #path('nashcode.com/<string : username>/resultadobusqueda',views.resultado_busqueda),
    #path('nashcode.com/<string : username>/publicar',views.publicar),
    #path('nashcode.com/<string : username>/editar/<int : id>',views.editar),
    #path('nashcode.com/<string : username>/publicacion/<int : id>',views.publicacion),
    #path('nashcode.com/<string : username>/perfil',views.perfil),
    #path('nashcode.com/<string : username>/miperfil',views.mi_perfil),
    #path('nashcode.com/<string : username>/editarperfil',views.editar_perfil),
]
