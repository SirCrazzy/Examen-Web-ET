from django.shortcuts import render
from .models import Categoria, Libro, Autor

def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/index.html', {'categorias': categorias})

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libros.html', {'libros': libros})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autores.html', {'autores': autores})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/categorias.html', {'categorias': categorias})
