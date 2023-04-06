from django.contrib import admin

from .models import Libro, Comentario

# Register your models here.
admin.site.register(Libro)
admin.site.register(Comentario)