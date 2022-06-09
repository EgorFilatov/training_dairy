from django.db import models
from django.urls import reverse_lazy


class TrainingPrograms(models.Model):
    program_name = models.CharField(verbose_name='Название тренировочной программы', max_length=150)
    program_description = models.TextField(blank=True, null=True, verbose_name='Описание тренировочной программы')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    training_weeks = models.ManyToManyField('Weeks', verbose_name='Тренировочная неделя')

    def get_absolute_url(self):
        return reverse_lazy('my_training_programs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.programs_name

    class Meta:
        verbose_name = 'Программа тренировок'
        verbose_name_plural = 'Программы тренировок'
        ordering = ['-created_at']


class Weeks(models.Model):
    number_of_week = models.CharField(verbose_name='Номер недели', max_length=5)
    training_days = models.ManyToManyField('Days', verbose_name='Тренировочный день')

    def get_absolute_url(self):
        return reverse_lazy('training_program_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.number_of_week

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'
        ordering = ['id']


class Days(models.Model):
    number_of_days = models.CharField(verbose_name='Номер дня', max_length=5)
    training_week = models.ForeignKey('Weeks', on_delete=models.PROTECT, verbose_name='Тренировочная неделя')
    exercizes = models.ManyToManyField('Exercizes', verbose_name='Тренировочная неделя')

    def get_absolute_url(self):
        return reverse_lazy('training_program_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.number_of_days

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'
        ordering = ['id']


class Exercizes(models.Model):
    exercize_name = models.CharField(verbose_name='Название упражнения', max_length=250)
    exercize_description = models.TextField(blank=True, null=True, verbose_name='Описание упражнения')
    exercize_link = models.CharField(verbose_name='Ссылка на упражнение', max_length=250)


    def get_absolute_url(self):
        return reverse_lazy('my_training_programs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.programs_name

    class Meta:
        verbose_name = 'Программа тренировок'
        verbose_name_plural = 'Программы тренировок'
        ordering = ['-created_at']
