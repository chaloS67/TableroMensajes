from django.db import models
# models.py

class Tablero(models.Model):
    texto = models.CharField(max_length=200),
    remitente = models.CharField(max_length=50),
    destinatario = models.CharField(max_length=10, choices=[('pendiente', 'Pendiente'),
    ('completado', 'Completado')]),

def __str__(self):
    return self.titulo
