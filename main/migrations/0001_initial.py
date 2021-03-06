# Generated by Django 4.0.5 on 2022-06-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_day', models.CharField(max_length=50, verbose_name='Название дня')),
                ('day_finished', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дни',
            },
        ),
        migrations.CreateModel(
            name='ExerciseCharacteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40')], default='0', max_length=2, verbose_name='Повторения')),
                ('sets', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Подходы')),
                ('weight', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вес')),
                ('difficulty_rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Оценка сложности')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
            ],
            options={
                'verbose_name': 'Характеристика упражнения',
                'verbose_name_plural': 'Характеристики упражнения',
            },
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=250, verbose_name='Название упражнения')),
                ('exercise_description', models.TextField(blank=True, null=True, verbose_name='Описание упражнения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/img/exercise_img/%Y/%m/%d/', verbose_name='Изображение')),
                ('exercise_link', models.CharField(max_length=250, verbose_name='Ссылка на упражнение')),
                ('exercise_finished', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Упражнение',
                'verbose_name_plural': 'Упражнения',
            },
        ),
        migrations.CreateModel(
            name='Weeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_week', models.CharField(max_length=50, verbose_name='Название недели')),
                ('week_finished', models.BooleanField(default=False)),
                ('training_days', models.ManyToManyField(to='main.days', verbose_name='Тренировочные дни')),
            ],
            options={
                'verbose_name': 'Тренировочная неделя',
                'verbose_name_plural': 'Тренировочные недели',
            },
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=150, verbose_name='Название тренировочной программы')),
                ('program_description', models.TextField(blank=True, null=True, verbose_name='Описание тренировочной программы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('program_finished', models.BooleanField(default=False)),
                ('training_weeks', models.ManyToManyField(to='main.weeks', verbose_name='Тренировочные недели')),
            ],
            options={
                'verbose_name': 'Программа тренировок',
                'verbose_name_plural': 'Программы тренировок',
            },
        ),
        migrations.AddField(
            model_name='days',
            name='exercise',
            field=models.ManyToManyField(to='main.exercises', verbose_name='Упражнения'),
        ),
        migrations.AddField(
            model_name='days',
            name='exercise_characteristics',
            field=models.ManyToManyField(to='main.exercisecharacteristics', verbose_name='Характеристики упражнений'),
        ),
    ]
