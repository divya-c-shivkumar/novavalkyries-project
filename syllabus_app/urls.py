from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pdf/<int:id>/', views.generate_pdf),
]
