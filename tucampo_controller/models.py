from django.db import models
from django.core.validators import RegexValidator, MinValueValidator #para evaluar los numeros 
# Create your models here.

#clase para la creacion de un usuario tomando en cuenta datos generales como especificos
class CreateUser(models.Model):
    name = models.CharField(max_length=25) 
    last_name = models.CharField(max_length=50)
    birthday = models.DateField( auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    city = models.CharField(max_length=50)
    estate = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    live_mexico = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=254)
    number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$' #El validador se hizo de este modo para corregir los numeros de telefono
            )
        ]
    )
    charge = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    enterprise = models.CharField(max_length=30)
    ubication = models.CharField(max_length=40)
    
#clase para el control de usuarios NOTA este no tendra relacion con crear usuario ya que el validador tendra acceso sobre estos   
class login(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(unique=True, max_length=30)
