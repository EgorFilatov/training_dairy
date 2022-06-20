from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .import urls
from .forms import ProgramsForm, WeeksChoiceForm
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


#class ProgramsCreate(CreateView):
#    form_class = ProgramsForm
#    template_name = 'main/programs_create.html'
#    success_url = reverse_lazy('my_programs')


def programs_create_1(request):
    if request.method == 'POST':
        programs_form = ProgramsForm(request.POST)
        weeks_choice_form = WeeksChoiceForm(request.POST)
        if programs_form.is_valid() and weeks_choice_form.is_valid():
            try:
                programs_form.save()
                Weeks.objects.create()
            except:
                programs_form.add_error(None, 'Ошибка добавления поста')
    else:
        programs_form = ProgramsForm()
        weeks_choice_form = WeeksChoiceForm()

    return render(request, 'main/programs_create.html', {'programs_form': programs_form, 'weeks_choice_form': weeks_choice_form})


def programs_create(request):
    if request.method == 'POST':
        programs_form = ProgramsForm(request.POST)
        weeks_choice_form = WeeksChoiceForm(request.POST)
        if programs_form.is_valid() :
            print(programs_form.cleaned_data)
            #programs_form.save()
            #Weeks.objects.create()
        else:
            programs_form = ProgramsForm()
            weeks_choice_form = WeeksChoiceForm()
        return render(request, 'main/programs_create.html', {'programs_form': programs_form, 'weeks_choice_form': weeks_choice_form})
