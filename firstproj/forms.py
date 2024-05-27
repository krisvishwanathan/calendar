# myapp/forms.py
from django import forms
from .models import Agent

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
