from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .import urls
from .models import Programs, Weeks


class ProgramsList(ListView):
    model = Programs
    template_name = 'main/my_programs.html'
    context_object_name = 'program'
    extra_context = {'breadcrumbs': 'Мои программы тренировок'}
    paginate_by = 20


class WeeksList(ListView):
    model = Weeks
    template_name = 'main/weeks_list.html'
    context_object_name = 'week'
    #program_name = Programs.
    extra_context = {'breadcrumbs': 'Тренировочные недели'}
    paginate_by = 20
