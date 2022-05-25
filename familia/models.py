from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Familia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, verbose_name='Nombre')
    apellido = models.CharField(max_length=45, verbose_name='Apellido')
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento AAAA-MM-DD')
    edad = models.IntegerField(verbose_name='Edad')
    email = models.EmailField(verbose_name='Email')
    telefono = models.CharField(max_length=16, verbose_name='Telefono')
    direccion = models.CharField(max_length=60, verbose_name='Direccion')
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    
    # Configuaración para mostrar la información en el administrador
    def __str__(self):
        info_familiar = 'Familiar ID: ' +  str(self.id) + '  - ' + self.nombre + ' ' + self.apellido 
        return info_familiar
    
    # Configuracion para eliminar una imagen y no quede guarda dentro de la carpeta imagenes
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    
