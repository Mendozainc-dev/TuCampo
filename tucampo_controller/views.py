from rest_framework import viewsets
from .serializer import CreateUser_Serializer
from .models import CreateUser
# Create your views here.

class CreateUser(viewsets.ModelViewSet):
    serializer_class = CreateUser_Serializer
    queryset = CreateUser.objects.all() #Administrador de consultas