
from app.views import inicio, agregar, editar, eliminar
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar/', agregar, name='agregar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('eliminar/<int:id>/', eliminar, name='eliminar')
]