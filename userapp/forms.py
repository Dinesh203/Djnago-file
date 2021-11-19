from django import forms
from .models import SignUp
from django.forms import ModelForm


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SignUp
        fields = "__all__"
