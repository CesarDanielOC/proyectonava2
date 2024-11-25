from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    id_paciente = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()  
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
