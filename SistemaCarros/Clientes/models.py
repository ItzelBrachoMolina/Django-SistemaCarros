from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField




class Clientes(models.Model):
    tipo = models.CharField(max_length=200)
    TITLE = (
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Mr.', 'Mr.'),
    )
    corporacion=models.CharField(max_length=200,blank=True)
    titulo = models.CharField(max_length=200, choices=TITLE,default='Mr.')
    nombre = models.CharField(max_length=200, blank=True)
    apellido = models.CharField(max_length=200,blank=True)
    telefono = models.IntegerField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    fax = models.IntegerField(blank=True, null=True)
    correo = models.EmailField(max_length=200,blank=True, null=True)
    website=models.URLField(max_length=200,blank=True, null=True)
    social_media=models.CharField(max_length=200,blank=True, null=True)
    social_media2=models.CharField(max_length=200,blank=True, null=True)
    social_media3=models.CharField(max_length=200,blank=True, null=True)
    contacto_alternativo=models.CharField(max_length=200,blank=True, null=True)
    contacto_alternativo2 = models.CharField(max_length=200,blank=True, null=True)
    contacto_alternativo3 = models.CharField(max_length=200,blank=True, null=True)
    pais = models.CharField(max_length=200,blank=True, null=True)
    direccion=models.CharField(max_length=200,blank=True, null=True)
    ciudad=models.CharField(max_length=255,blank=True, null=True)
    estado=models.CharField(max_length=255,blank=True, null=True)
    zip=models.CharField(max_length=255,blank=True, null=True)
    fecha_registro = models.DateTimeField(default=datetime.now,blank=True, null=True)



    def __str__(self):
        return f'{self.nombre} {self.apellido}'


