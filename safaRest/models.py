from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class TipoRestaurante(models.TextChoices):
    ITALIANO="Italiano"
    TAILANDES="Tailandes"
    INDIO="Indio"

    def mostrar_tipo(self):
        return self.value

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

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email válido")
        user=self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    
  class Roles(models.TextChoices):
    ADMIN = "Admin"
    PROPIETARIO_RESTAURANTE = "Propietario"
    CLIENTE = "Cliente"

    def mostrar(self):
        return self

class Usuario(AbstractBaseUser, PermissionsMixin): #AbstractBaseUser sustituye al usuario por defecto creado en el admin
                                                    #PermissionsMixin le da permisos al usuario
    email=models.EmailField(unique=True)
    username=models.CharField(unique=True, max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    rol = models.CharField(max_length=60, choices=Roles.choices,default=Roles.CLIENTE)
    is_active = models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['username, email, password']

    objects=UsuarioManager()

    def __str__(self):
        return self.username, self.email




