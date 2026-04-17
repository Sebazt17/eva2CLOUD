from django.urls import path
from . import views

urlpatterns = [
    path('carrusel/', views.vista_carrusel, name='carrusel'),
]