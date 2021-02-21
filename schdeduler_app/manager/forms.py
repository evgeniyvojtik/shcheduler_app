from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, CharField, PasswordInput, Textarea, DateField, DateInput, TimeInput

from manager.models import Event


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass

    username = UsernameField(widget=TextInput(attrs={"class": "form-control"}))
    password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control"})
    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control"}),
        strip=False
    )


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'autofocus': True, "class": "form-control"}))
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password', "class": "form-control"}),
    )

class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date_from', 'start_time', 'date_till', 'end_time', 'description']
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control", "rows": 5, "cols": 50}),
            'date_from': DateInput(attrs={'class': 'form-control', 'placeholder': 'Select start date', 'type': 'date'}),
            'start_time': TimeInput(attrs={'class': 'form-control', 'placeholder': 'Select start time', 'type': 'time'}),
            'date_till': DateInput(attrs={'class': 'form-control', 'placeholder': 'Select end date', 'type': 'date'}),
            'end_time': TimeInput(attrs={'class': 'form-control', 'placeholder': 'Select end time', 'type': 'time'}),
        }
