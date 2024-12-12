import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import UpperTextModel, CustomUser


def validate_only_letters(value):
    """ Кастомний валідатор: перевіряє, що текст містить лише літери."""
    if not re.match(r'^[a-zA-Z]+$', value):
        raise ValidationError('Текст повинен містити тільки наступні літери: (a-z, A-Z).')


class UpperTextForm(forms.ModelForm):
    class Meta:
        model = UpperTextModel
        validators = [validate_only_letters]
        fields = ['upper_text']
        labels = {
            'upper_text': 'Введіть текст:'
        }
        widget = forms.TextInput(attrs={'placeholder': 'Введіть тільки латинські літери...'})


class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, label="Телефон",
                                   required=True,
                                   help_text="Введіть номер телефону за форматом:  +380234567890."
                                   )

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^+\d{12}$', phone_number):
            raise forms.ValidationError("Невірний формат номера телефону!")
        return phone_number
