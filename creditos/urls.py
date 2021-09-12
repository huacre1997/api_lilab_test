from django.urls import path,include
from creditos.views import *
urlpatterns = [
    path("usuarios/",usuario_api_view,name="lista-usuarios"),
    path("clientes/",cliente_api_view,name="lista-cliente"),
    path("solicitudes/",solicitud_api_view,name="lista-solicitudes"),
    path("solicitudes/<int:pk>",solicitud_detalle_api_view,name="detalle-solicitud")
    
]
