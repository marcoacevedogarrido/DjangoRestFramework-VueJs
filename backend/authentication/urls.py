
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication.api.usuario import  LoginView, LogoutView, RegisterView

urlpatterns = [
    path('api/login', LoginView.as_view()),
    path('api/logout', LogoutView.as_view()),
    path('api/register', RegisterView.as_view())


]

urlpatterns = format_suffix_patterns(urlpatterns)
