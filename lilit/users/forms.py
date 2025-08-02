from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    class Meta:
        model=get_user_model()
        fields=['username','password']

class RegisterUserForm(UserCreationForm):

    class Meta:
        model=get_user_model()
        fields=['username','email', 'password1', 'password2']

    def cleaned_email(self):
        email=self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("E-mail already exists")
        return email