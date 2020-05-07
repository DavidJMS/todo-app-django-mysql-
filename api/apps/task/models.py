from django.db import models


class Task(models.Model):
    id 			= models.AutoField(primary_key=True) 
    title 		= models.CharField(max_length=70,null=True,verbose_name='Título')
    description = models.CharField(max_length=200, blank=False,null=True,verbose_name='descripción')
    created     = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creación De La Tarea')
    completed 	= models.BooleanField(default=False,verbose_name='Completado')

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["-created"]

    def __str__(self):
        return self.title