from django import forms 
from .models import Person 

class CreateNewPerson(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','lastname','email']
        