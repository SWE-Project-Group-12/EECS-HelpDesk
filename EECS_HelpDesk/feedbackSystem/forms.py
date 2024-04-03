from django import forms
from .models import Feedback
from django.core.validators import ValidationError


class FeedbackForm(forms.Form):
    feature = forms.CharField(widget=forms.Textarea, required=True)
    rating = forms.CharField(widget=forms.TextInput(attrs={'min': 1,'max': 5,'type': 'number'}), required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)


    def clean_rating(self):
        rating = self.cleaned_data.get("rating")

        if not str(rating).isnumeric():
            raise ValidationError("Rating must be a number between 1 and 5.")

        if int(rating) < 1 or int(rating) > 5:
            raise ValidationError("Rating must be a number between 1 and 5.")

        return rating