from rest_framework import serializers, viewsets
from server.models import Proceso
from server.api.documentos import DocumentoSerializer
from server.api.clientes import ClienteSerializer
from server.api.productos import ProductoSerializer
from rest_framework import views


class ProcesoSerializer(serializers.ModelSerializer):
    documento_obj = DocumentoSerializer(source='documento', read_only=True)
    cliente_obj = ClienteSerializer(source='cliente')
    producto_obj = ProductoSerializer(source='producto')
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Proceso
        fields = ['id', 'cantidad', 'documento_obj', 'cliente_obj', 'producto_obj']

    def create(self, validated_data):
        return Proceso.objects.create(**validated_data)

class ProcesoView(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
