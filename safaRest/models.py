from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class TipoRestaurante(models.TextChoices):
    ITALIANO="Italiano"
    TAILANDES="Tailandes"
    INDIO="Indio"

class Restaurante(models.Model):
    nombre=models.CharField(max_length=150)
    ciudad=models.CharField(max_length=150)
    tipo=models.CharField(max_length=60, choices=TipoRestaurante.choices)
    capacidad=models.IntegerField()
    fecha_fundacion=models.DateField()
    # ctrl+espacio dentro del paréntesis para ver las opciones. Ej: DateField()

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre=models.CharField(max_length=150)
    precio=models.FloatField()
    restaurante=models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + "----" + str(self.precio)



