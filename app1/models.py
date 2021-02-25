from django.db import models
from ckeditor.fields import RichTextField

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    alias =  models.CharField(max_length = 20)
    nombre =  models.CharField(max_length = 60)
    email =  models.CharField(max_length = 60)
    password =  models.CharField(max_length = 10)
    likes = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 30)
    descripcion = models.TextField()
    categoria = models.CharField(max_length = 10)
    codigo = RichTextField(blank = True,null = True)
    referencia = RichTextField(blank = True,null = True)
    likes = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

class Relacion(models.Model):
    usuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, null = True, blank = True, on_delete = models.CASCADE)
    like = models.IntegerField()
    guardado = models.IntegerField()
