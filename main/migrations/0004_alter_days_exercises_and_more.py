# Generated by Django 4.0.5 on 2022-06-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_exercise_days_exercises_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='exercises',
            field=models.ManyToManyField(blank=True, null=True, to='main.exercises', verbose_name='Упражнения'),
        ),
        migrations.AlterField(
            model_name='days',
            name='exercises_characteristics',
            field=models.ManyToManyField(blank=True, null=True, to='main.exercisecharacteristics', verbose_name='Характеристики упражнений'),
        ),
        migrations.AlterField(
            model_name='exercisecharacteristics',
            name='difficulty_rating',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True, verbose_name='Оценка сложности'),
        ),
        migrations.AlterField(
            model_name='exercisecharacteristics',
            name='reps',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40')], default='0', max_length=2, null=True, verbose_name='Повторения'),
        ),
        migrations.AlterField(
            model_name='exercisecharacteristics',
            name='sets',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True, verbose_name='Подходы'),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='exercise_finished',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Упражнение завершено'),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='exercise_link',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на упражнение'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='program_finished',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Программа завершена'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='training_weeks',
            field=models.ManyToManyField(blank=True, null=True, to='main.weeks', verbose_name='Тренировочные недели'),
        ),
        migrations.AlterField(
            model_name='weeks',
            name='training_days',
            field=models.ManyToManyField(blank=True, null=True, to='main.days', verbose_name='Тренировочные дни'),
        ),
    ]