from django.db import models
from django.urls import reverse_lazy


class Programs(models.Model):
    program_name = models.CharField(verbose_name='Название тренировочной программы', max_length=150)
    program_description = models.TextField(blank=True, null=True, verbose_name='Описание тренировочной программы')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    training_weeks = models.ManyToManyField('Weeks', verbose_name='Тренировочные недели')
    program_finished = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('weeks_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.program_name

    class Meta:
        verbose_name = 'Программа тренировок'
        verbose_name_plural = 'Программы тренировок'


class Weeks(models.Model):
    name_of_week = models.CharField(verbose_name='Название недели', max_length=50)
    training_days = models.ManyToManyField('Days', verbose_name='Тренировочные дни')
    week_finished = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('weeks_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name_of_week

    class Meta:
        verbose_name = 'Тренировочная неделя'
        verbose_name_plural = 'Тренировочные недели'


class Days(models.Model):
    name_of_day = models.CharField(verbose_name='Название дня', max_length=50)
    exercise = models.ManyToManyField('Exercises', verbose_name='Упражнения')
    exercise_characteristics = models.ManyToManyField('ExerciseCharacteristics', verbose_name='Характеристики упражнений')
    day_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name_of_day

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class Exercises(models.Model):
    exercise_name = models.CharField(verbose_name='Название упражнения', max_length=250)
    exercise_description = models.TextField(blank=True, null=True, verbose_name='Описание упражнения')
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='media/img/exercise_img/%Y/%m/%d/')
    exercise_link = models.CharField(verbose_name='Ссылка на упражнение', max_length=250)
    exercise_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.exercise_name

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class ExerciseCharacteristics(models.Model):
    CHOICES = [
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
        ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'),
        ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'),
        ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'),
        ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'),
    ]
    reps = models.CharField(verbose_name='Повторения', max_length=2, choices=CHOICES, default='0')
    sets = models.CharField(verbose_name='Подходы', max_length=2, choices=CHOICES[0:11], default='0')
    weight = models.CharField(blank=True, null=True, verbose_name='Вес', max_length=50)
    difficulty_rating = models.CharField(verbose_name='Оценка сложности', max_length=2, choices=CHOICES[0:11], default='0')
    comments = models.TextField(blank=True, null=True, verbose_name='Комментарии')

    def get_absolute_url(self):
        return reverse_lazy('my_training_programs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.reps

    class Meta:
        verbose_name = 'Характеристика упражнения'
        verbose_name_plural = 'Характеристики упражнения'
