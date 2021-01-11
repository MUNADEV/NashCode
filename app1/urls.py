from django.urls import path,include
from . import views

urlpatterns = [
    path('nashcode.com',views.index),
    path('nashcode.com/inicio_sesion',views.inicio_sesion),
    path('nashcode.com/registro',views.registro),
    path('nashcode.com/<str:username>/home',views.home),
    path('nashcode.com/<str:username>/guardado',views.guardado),
    path('nashcode.com/<str:username>/busqueda',views.busqueda),
    path('nashcode.com/<str:username>/resultadobusqueda',views.resultado_busqueda),
    #path('nashcode.com/<str:username>/publicar',views.publicar),
    path('nashcode.com/publicar',views.publicar),
    #path('nashcode.com/<str:username>/editar/<int:id>',views.editar),
    path('nashcode.com/editar',views.editar),
    #path('nashcode.com/<str:username>/publicacion/<int:id>',views.publicacion),
    path('nashcode.com/publicacion',views.publicacion),
    path('nashcode.com/<str:username>/perfil',views.perfil),
    path('nashcode.com/<str:username>/miperfil',views.mi_perfil),
    path('nashcode.com/<str:username>/editarperfil',views.editar_perfil),
]
