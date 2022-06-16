from django import forms
from .models import Programs


class ProgramsForm(forms.ModelForm):
    #category = forms.ModelChoiceField(empty_label=None, queryset=Categories.objects.all())
    class Meta():
        model = Programs
        fields = ['program_name', 'program_description', 'training_weeks']
        widgets = {
            'program_name': forms.TextInput(attrs={'class': 'form-control'}),
            'program_description': forms.Textarea(attrs={'class': 'form-control'}),
            'training_weeks': forms.SelectMultiple(attrs={'class': 'form-control'}),}
