from app.views import inicio
from django.urls import path

urlpatterns = [
    path('', inicio, name='indice'),
]