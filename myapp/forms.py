from django import forms
from .models import Employee

# class EmployeeForm(forms.Form):
#     name=forms.CharField(max_length="15")
#     address=forms.CharField(widget=forms.Textarea)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        # fields=["name"]

