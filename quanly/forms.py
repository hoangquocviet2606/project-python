from quanly.models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'