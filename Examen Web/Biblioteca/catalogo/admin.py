from django.contrib import admin
from .models import Categoria, Libro, Autor

admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Autor)