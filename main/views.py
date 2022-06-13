from django.shortcuts import render
from django.core.paginator import Paginator
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
    weeks = Programs.objects.values_list('training_weeks__name_of_week')
    extra_context = {'breadcrumbs': 'Тренировочные недели', 'weeks': weeks}
    paginate_by = 20


def weeks_list(request, pk):
    weeks = Programs.objects.filter(pk=pk).values('training_weeks__name_of_week', 'training_weeks__week_finished')
    return render(request, 'main/weeks_list.html', {'weeks': weeks, })