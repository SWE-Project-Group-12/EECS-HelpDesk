from django import forms
from ..models import STATUS_CHOICES, PRIORITY_CHOICES
from django.core.validators import ValidationError


class BaseTicketDetails(forms.Form):
    # Abstract Form (Similar to abstract models, see https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the common form headings for an EC Form and Technical Fault Form.

    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))

    # ////////////////////////////////////////////////////////////////
    # i commented these out otherwise the form will not work since it complains they are required
    # you can add required param and set to false 
    # but i think best to not use them at all since these fields are gonna be entered using defualt values from the model (which is what you want no?)
    # ////////////////////////////////////////////////////////////////


    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICES,
    #     disabled=True,
    #     widget=forms.Select(attrs={
    #         'class' : 'form-control'
    #     })
    # )

    # dateCreated = forms.DateField(disabled=True)
    # username = forms.CharField(max_length=10, min_length=7, required=True, widget=forms.HiddenInput)

    class Meta: 
        abstract = True


    def clean_priority(self):
        priority = self.cleaned_data.get("priority")

        if priority not in PRIORITY_CHOICES.keys():
            raise ValidationError("You must choose one of the priortity values provided.")

        return priority