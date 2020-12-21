from django.urls import path
from rest_framework import routers
from server.api.clientes import ClienteView
from server.api.procesos import ProcesoView
from server.api.productos import ProductoView
from server.api.documentos import DocumentoView

router = routers.SimpleRouter()

router.register(r'api/clientes', ClienteView, 'clientes'),
router.register(r'api/procesos', ProcesoView, 'procesos')
router.register(r'api/productos', ProductoView, 'productos')
router.register(r'api/documentos', DocumentoView, 'documentos')


urlpatterns = []
urlpatterns += router.urls