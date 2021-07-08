
from app.views import inicio, agregar
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar/', agregar, name='agregar'),
]