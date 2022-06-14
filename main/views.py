from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .import urls
from .models import Programs, Weeks, Days


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
    weeks = Programs.objects.values_list('training_weeks__name_of_week')
    extra_context = {'breadcrumbs': 'Тренировочные недели', 'weeks': weeks}
    paginate_by = 20


def weeks_list(request, pk):
    weeks = Programs.objects.get(pk=pk).training_weeks.all()
    return render(request, 'main/weeks_list.html', {'weeks': weeks, })


def days_list(request, pk):
    days = Weeks.objects.get(pk=pk).training_days.all()
    return render(request, 'main/days_list.html', {'days': days, })


def exercises_list(request, pk):
    exercises = Days.objects.get(pk=pk).exercises.all()
    return render(request, 'main/exercises_list.html', {'exercises': exercises, })


class ProgramsCreate(CreateView):
    form_class = Programs
    template_name = 'main/news_add.html'
    success_url = reverse_lazy('my_programs')

