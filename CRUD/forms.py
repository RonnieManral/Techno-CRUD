from django import forms
from django.db.models import fields
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                    'firstname':forms.TextInput(attrs={'class':'form-control'}),
                    'lastname':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.TextInput(attrs={'class':'form-control'}),
        }