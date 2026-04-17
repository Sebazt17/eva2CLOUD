from django.db import models

class Galeria(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='carrusel/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo