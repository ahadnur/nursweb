from .models import Problem
from django import forms


class ProblemForm(forms.ModelForm):
    """Form definition for Problem."""

    class Meta:
        """Meta definition for Problemform."""

        model = Problem
        fields = ('title', 'body', 'problem_setter',)
