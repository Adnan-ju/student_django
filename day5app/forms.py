

from django import forms
from .models import Student,Course

class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

