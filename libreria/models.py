from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    resena = models.TextField(verbose_name="Reseña", null=True)
    

    def __str__(self):
        return f"Titulo: {self.titulo} - Reseña: {self.resena}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super(Libro, self).delete(using=using, keep_parents=keep_parents)

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    def __str__(self):
        return f"{self.autor.username} ({self.fecha})"
