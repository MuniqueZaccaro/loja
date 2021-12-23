from django.urls import path
from . import views

urlpatterns = [
    path('registrar_entrega/', views.registrar_entrega),
]