from rest_framework import serializers, viewsets
from server.models import Cliente
from rest_framework import views
# from rest_framework.permissions import IsAuthenticated


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticated]
