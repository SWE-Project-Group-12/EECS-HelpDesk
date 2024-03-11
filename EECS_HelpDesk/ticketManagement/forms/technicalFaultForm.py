from django import forms
from .baseTicketDetails import BaseTicketDetails

class TechnicalFaultForm(BaseTicketDetails):
    # ModelForm. Based on the Model TechnicalFault.
    # Inherits form headings from Base Ticket Details.
    # Used to validate Technical Faults.

    LOCATION_CHOICES = {
        "ITL" : "ITL",
        "ITS" : "ITS",
        "LIBRARY" : "Library",
        "NONE" : "None",
    }

    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class' : 'form-control'
        })
    )
