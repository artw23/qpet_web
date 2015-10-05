from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length = 10)
    correo = models.CharField(max_length = 40)
    password = models.CharField(max_length = 150)
    salt = models.CharField(max_length = 150)
    estado = models.IntegerField()
    rol = models.IntegerField()
    fecha_registo = models.DateTimeField(auto_now_add=True)
    ultimo_conectado = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.telefono