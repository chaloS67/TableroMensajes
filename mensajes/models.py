from django.db import models
# models.py

class Tablero(models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.titulo

