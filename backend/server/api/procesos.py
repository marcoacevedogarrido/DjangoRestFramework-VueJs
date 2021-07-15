from rest_framework import serializers, viewsets
from server.models import Proceso
from server.api.documentos import DocumentoSerializer
from server.api.clientes import ClienteSerializer
from server.api.productos import ProductoSerializer
from rest_framework import views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProcesoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # documento_obj = DocumentoSerializer(source='documento', read_only=True)
    # cliente_obj = ClienteSerializer(source='cliente')
    # producto_obj = ProductoSerializer(source='producto')

    class Meta:
        model = Proceso
        fields = ['id', 'cantidad', 'documento', 'cliente', 'producto', 'owner',]


class ProcesoView(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
