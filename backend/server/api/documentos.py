from rest_framework import serializers, viewsets
from server.models import Documento
from rest_framework import views
from server.api.clientes import ClienteSerializer


class DocumentoSerializer(serializers.ModelSerializer):
    cliente_obj = ClienteSerializer(source='cliente')

    class Meta:
        model = Documento
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_envio', 'cliente_obj']


class DocumentoView(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
