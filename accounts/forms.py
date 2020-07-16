from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django import forms


class RegisterForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'company', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
