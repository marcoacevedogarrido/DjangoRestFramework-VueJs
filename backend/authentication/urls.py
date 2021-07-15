from django.urls import path
from rest_framework import routers
from authentication.api.usuario import UserViewSet

router = routers.SimpleRouter()

router.register(r'api/usuarios', UserViewSet, 'usuarios')

urlpatterns = []
urlpatterns += router.urls
