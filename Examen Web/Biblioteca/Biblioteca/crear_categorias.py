import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Biblioteca.settings')
django.setup()

from catalogo.models import Categoria

# Crear categorías
Categoria.objects.create(nombre='Ciencia Ficción')
Categoria.objects.create(nombre='Fantasía')
Categoria.objects.create(nombre='Historia')

print('Categorías creadas con éxito')
