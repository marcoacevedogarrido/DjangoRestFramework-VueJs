from django.urls import path
from rest_framework import routers
from server.api.clientes import ClienteView
from server.api.procesos import ProcesoView
from server.api.productos import ProductoView
from server.api.documentos import DocumentoView
from server.api.usuarios import Usuariosview
from server.api.sorteos import SorteoView
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import include, url
from server.api.pandas import PandasView

router = routers.SimpleRouter()

router.register(r'api/clientes', ClienteView, 'clientes'),
router.register(r'api/procesos', ProcesoView, 'procesos')
router.register(r'api/productos', ProductoView, 'productos')
router.register(r'api/documentos', DocumentoView, 'documentos'),
router.register(r'api/sorteos', SorteoView, 'sorteos'),
router.register(r'api/usuarios', Usuariosview, 'usuarios')



urlpatterns = [ url(r'^data', PandasView.as_view()), ]
urlpatterns += router.urls
