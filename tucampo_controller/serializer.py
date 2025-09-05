from rest_framework import serializers
from .models import CreateUser

class CreateUser_Serializer(serializers.ModelSerializer):
    class Meta: #Recordar poner Meta en el codigo con mayuscula me dio error jajajaja
        model = CreateUser
        fields = '__all__'