from django import forms
from movies.models import Movies

# form definition

class movieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'
