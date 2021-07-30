from rest_framework import serializers, viewsets
from server.models import Producto
from rest_framework import views
from rest_framework.permissions import IsAuthenticated

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
