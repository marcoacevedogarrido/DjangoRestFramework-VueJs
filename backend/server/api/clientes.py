from rest_framework import serializers, viewsets
from server.models import Cliente
from rest_framework import views

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['id',
                  'nombre',
                  'razon_social',
                  'rut'
                  ]


class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
