from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target_value', 'current_value']

"""class UsersForm(forms):
    class Meta:
        model = Users
        fields = ['username', 'email']"""