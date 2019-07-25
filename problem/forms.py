from .models import Problem
from django import forms


class ProblemForm(forms.ModelForm):
    """Form definition for Problem."""

    class Meta:
        """Meta definition for Problemform."""

        model = Problem
        fields = ['title', 'body', 'problem_setter']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'problem_setter': forms.TextInput(attrs={'class': 'form-control'})
        }
