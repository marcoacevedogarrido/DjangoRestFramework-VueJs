from django.urls import path
from rest_framework import routers
from authentication.api.usuario import RegistroUsuario


router = routers.SimpleRouter()

router.register(r'usuarios', RegistroUsuario, 'usuarios')


urlpatterns = []
urlpatterns += router.urls
