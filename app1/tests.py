from django.test import TestCase
from django.template.defaultfilters import slugify
from app1.models import Publicacion
from django.urls import resolve,reverse

class UrlTest(TestCase):
    
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    def test_inicio_sesion(self):
        response = self.client.get(reverse('inicio_sesion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio_sesion.html')
    def test_registro(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro.html')

    '''
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'index.html')
    def test_busqueda(self):
        response = self.client.get(reverse('busqueda'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busqueda.html')
    def test_resultado_busqueda(self):
        response = self.client.get(reverse('resultado_busqueda'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resultado_busqueda.html')
    def test_publicar(self):
        response = self.client.get(reverse('publicar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publicar.html')
    def test_editar(self):
        response = self.client.get(reverse('editar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar.html')
    def test_publicacion(self):
        response = self.client.get(reverse('publicacion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publicacion.html')
    def test_perfil(self):
        response = self.client.get(reverse('perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')
    def test_editar_perfil(self):
        response = self.client.get(reverse('editar_perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_perfil.html')

      
    '''