from django.urls import path
from . import views  # views modülünü eklediğimizden emin olalım

urlpatterns = [
    path('filtrele/', views.filtrele, name='filtrele'),  # filtrele view'ine yönlendirme
]
