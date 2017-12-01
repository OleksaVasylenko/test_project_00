from django.forms import EmailField, TextInput
from django.contrib.auth import get_user_model, forms


class SignupForm(forms.UserCreationForm):
    email = EmailField(max_length=200, help_text='Required')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class SigninForm(forms.AuthenticationForm):
    username = EmailField(
        label='Email',
        max_length=254,
        widget=TextInput(attrs={'autofocus': True}),
    )
