from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, help_text='Ingrese una categoría de libro (e.g. Ciencia Ficción)')
    descripcion = models.TextField(max_length=1000, help_text='Ingrese una breve descripción de la categoría', default='No description')

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=200, help_text='Ingrese el nombre del autor')

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
