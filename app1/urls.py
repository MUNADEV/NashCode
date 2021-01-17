from django.urls import path,include
from . import views

urlpatterns = [
    path('nashcode.com',views.index),
    path('nashcode.com/inicio_sesion',views.inicio_sesion),
    path('nashcode.com/registro',views.registro),
    path('nashcode.com/home',views.home),
    path('nashcode.com/guardado',views.guardado),
    path('nashcode.com/busqueda',views.busqueda),
    path('nashcode.com/resultado_busqueda',views.resultado_busqueda),
    path('nashcode.com/publicar',views.publicar),
    path('nashcode.com/editar/<int:id>',views.editar),
    path('nashcode.com/publicacion/<int:id>',views.publicacion),
    path('nashcode.com/perfil/<int:id>',views.perfil),
    path('nashcode.com/editar_perfil',views.editar_perfil),
]
