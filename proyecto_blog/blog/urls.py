from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='blog-inicio'),
    path('about/', views.acerca_de, name='blog-about'),
]