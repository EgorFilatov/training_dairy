from django.shortcuts import render
from .import urls

def my_training_programs(request):
    return render(request, "main/my_training_programs.html", {})
