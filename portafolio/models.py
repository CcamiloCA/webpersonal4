from venv import create
from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200,verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(upload_to='projects',verbose_name="Imagen")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    update=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=['-created']

    def __str__(self):
        return self.title
