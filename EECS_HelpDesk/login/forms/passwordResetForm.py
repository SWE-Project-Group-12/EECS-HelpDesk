from django import forms
from django.core.validators import ValidationError


class PasswordResetForm(forms.Form):
    newPassword = forms.CharField(
        label="New Password:",
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput(),
        help_text="Must contain: \n"
                    "8 characters \n"
                    "1 capital letter \n"
                    "1 number"
    )

    verifyPassword = forms.CharField(
        label="Verify Password:",
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput(),
        help_text="Must contain: \n"
                    "8 characters \n"
                    "1 capital letter \n"
                    "1 number \n"
                    "matches your new password above."
    )

    def clean(self):
        newPassword = self.cleaned_data.get("newPassword")
        verifyPassword = self.cleaned_data.get("verifyPassword")

        if newPassword != verifyPassword:
            raise ValidationError("Passwords don't match.")

        return self.cleaned_data