from django.urls import path
from . import views

urlpatterns = [
    path('rentaiha/', views.Iha, name="rentaiha")
]