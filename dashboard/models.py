from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(max_length=255, null=False)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    

