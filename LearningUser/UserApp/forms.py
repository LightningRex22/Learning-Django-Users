from django import forms
from .models import *

class FacultyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Faculty
        fields = ['first_name','last_name','email','password','confirm_password','degree','department','course','subject']