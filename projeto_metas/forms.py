from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target_value', 'current_value']
        widgets ={
            'current_value': forms.NumberInput(attrs={
                'type':'range',
                'class': 'form-range',
                'min':'0',
                'max': '10',
                'step':'1',
                
            })
        }

"""class UsersForm(forms):
    class Meta:
        model = Users
        fields = ['username', 'email']"""