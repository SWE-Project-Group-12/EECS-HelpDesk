from django import forms


class BaseUserDetails(forms.Form):
    # Abstract Form (Similar to abstract models, see https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the form headings for both the Create User Form and the Login Form.

    # Decision made that username has to have at least 7 digits
    username = forms.CharField(min_length=7,
                               max_length=10,
                               help_text="Must be at least 7 characters long")
    # password has to be at least 8 digits
    password = forms.CharField(min_length=8,
                               max_length=128,
                               widget=forms.PasswordInput(),
                               help_text="Must contain: \n"
                                         "8 characters \n"
                                         "1 capital letter \n"
                                         "1 number")

    class Meta:
        abstract = True




