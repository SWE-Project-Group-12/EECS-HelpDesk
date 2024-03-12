from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
import baseUserDetails
from django.core.exceptions import ValidationError
# Used for djangos translation of texts
from django.utils.translation import gettext_lazy as simpletranslate

class CreateUserForm(baseUserDetails):
    # Inherits from BaseUserDetails Form.
    # Form is used to create new users.

    name = forms.CharField(min_length=4, max_length=25)
    surname = forms.CharField(max_length=25)

    def clean_name(self):
        name_data = self.cleaned_data['name']
        number = False

        for letter in range(0, len(name_data)):
            if name_data[letter].isdigit():
                number = True

        if number:
            return ValidationError(simpletranslate("Please do not include numbers in your name field"), code='invalid')

        return name_data

    def clean_surname(self):
        surname_data = self.cleaned_data['surname']
        number = False

        for letter in range(0, len(surname_data)):
            if surname_data[letter].isdigit():
                number = True

        if number:
            return ValidationError(simpletranslate("Please do not include numbers in your surname field"), code='invalid')

        return surname_data

    def clean_password(self):
        password_data = self.cleaned_data['password']
        capital_letter = False
        number = False

        for letter in range(0, len(password_data)):
            if capital_letter and number:
                break
            if password_data[letter].isupper():
                capital_letter = True
            if password_data[letter].isdigit():
                number = True

        if not capital_letter:
            return ValidationError(simpletranslate("Please add a capital letter"), code='invalid')
        if not number:
            return ValidationError(simpletranslate("Please add a number", code='invalid'))

        return password_data

    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'password']


