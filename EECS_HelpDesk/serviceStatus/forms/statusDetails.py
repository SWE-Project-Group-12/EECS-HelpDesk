from django import forms
from ..models import SERVICE_STATUS_CHOICES

class statusDetails(forms.Form):
    # Abstract Form (Similar to abstract models, see https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the form headings for both the Create User Form and the Login Form.

    status = forms.ChoiceField(choices=SERVICE_STATUS_CHOICES)

    status_description = forms.CharField(initial="" ,max_length= 200,
                                         help_text="Must be at least 5 characters long",
                                         label="Status Description", required=False)