from django.urls import path
from .views.usuario_view import UsuarioView

urlpatterns = [
    path('usuario', UsuarioView.as_view()),
    path('usuario/<int:pk>', UsuarioView.as_view())
]