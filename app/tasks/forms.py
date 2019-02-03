from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'status',
        ]
        labels = {
            'name': 'name',
            'status': 'status',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }
