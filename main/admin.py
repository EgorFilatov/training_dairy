from django.contrib import admin
from django import forms
from .models import Programs, Weeks, Days, Exercises, ExerciseCharacteristics


class ProgramsAdmin(admin.ModelAdmin):
    list_display = ['id', 'program_name', 'program_description', 'created_at', 'updated_at', ]
    list_display_links = ['id', 'program_name', ]
    search_fields = ['id', 'program_name', 'program_description', 'created_at', 'updated_at', ]


admin.site.register(Programs, ProgramsAdmin)


class WeeksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_of_week', ]
    list_display_links = ['id', 'name_of_week', ]
    search_fields = ['id', 'name_of_week', ]


admin.site.register(Weeks, WeeksAdmin)


class DaysAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_of_day', ]
    list_display_links = ['id', 'name_of_day', ]
    search_fields = ['id', 'name_of_day', ]


admin.site.register(Days, DaysAdmin)


class ExercisesAdmin(admin.ModelAdmin):
    list_display = ['id', 'exercise_name', 'exercise_description', 'image', 'exercise_link', ]
    list_display_links = ['id', 'exercise_name', ]
    search_fields = ['id', 'exercise_name', 'exercise_description', 'image', 'exercise_link', ]


admin.site.register(Exercises, ExercisesAdmin)


class ExerciseCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ['id', 'reps', 'sets', 'weight', 'difficulty_rating', 'comments', ]
    list_display_links = ['id', 'reps', ]
    search_fields = ['id', 'reps', 'sets', 'weight', 'difficulty_rating', 'comments', ]


admin.site.register(ExerciseCharacteristics, ExerciseCharacteristicsAdmin)
