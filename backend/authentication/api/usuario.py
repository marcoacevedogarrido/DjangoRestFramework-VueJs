from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        Instance = User()
        Instance.first_name = validate_data.get('first_name')
        Instance.last_name = validate_data.get('last_name')
        Instance.username = validate_data.get('username')
        Instance.email = validate_data.get('email')
        Instance.set_password(validate_data.get('password'))
        Instance.save()
        return Instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) !=0 :
            raise serializers.ValidationError('este user ya existe')
        else:
            return data


class RegistroUsuario(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            user= serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
