from django.contrib import admin
from django.urls import path
from .import views
from .views import ProgramsList, ProgramsCreate

urlpatterns = [
    path('', ProgramsList.as_view(), name='my_programs'),
    path('weeks_list/<int:pk>/', views.weeks_list, name='weeks_list'),
    path('days_list/<int:pk>/', views.days_list, name='days_list'),
    path('exercises_list/<int:pk>/', views.exercises_list, name='exercises_list'),
    path('programs_create/', ProgramsCreate.as_view(), name='programs_create'),
]
