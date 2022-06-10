from django.contrib import admin
from django.urls import path
from .import views
from .views import ProgramsList, WeeksList

urlpatterns = [
    path('', ProgramsList.as_view(), name='my_programs'),
    path('weeks_list', WeeksList.as_view(), name='weeks_list'),
]
