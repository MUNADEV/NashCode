from django.urls import path,include
from . import views 


urlpatterns = [
    path('nashcode.com',views.index,name='index'),
    path('nashcode.com/inicio_sesion',views.inicio_sesion,name='inicio_sesion'),
    path('nashcode.com/registro',views.registro,name='registro'),
    path('nashcode.com/home',views.home,name='home'),
    path('nashcode.com/guardado',views.guardado,name='guardado'),
    path('nashcode.com/busqueda',views.busqueda,name='busqueda'),
    path('nashcode.com/resultado_busqueda',views.resultado_busqueda,name='resultado_busqueda'),
    path('nashcode.com/publicar',views.publicar,name='publicar'),
    path('nashcode.com/editar/<int:id>',views.editar,name='editar'),
    path('nashcode.com/publicacion/<int:id>',views.publicacion,name='publicacion'),
    path('nashcode.com/perfil/<int:id>',views.perfil,name='perfil'),
    path('nashcode.com/editar_perfil',views.editar_perfil,name='editar_perfil'),
]
