from django.contrib import admin
from django.urls import path
from .import views
from .views import my_training_programs

urlpatterns = [
    path('', views.my_training_programs, name='my_training_programs'),
]
