from django import forms
from .baseTicketDetails import BaseTicketDetails
from ..models import TechnicalFault

class TechnicalFaultForm(BaseTicketDetails):
    # ModelForm. Based on the Model TechnicalFault.
    # Inherits form headings from Base Ticket Details.
    # Used to validate Technical Faults.


    location = forms.ChoiceField(
        choices=TechnicalFault.LOCATION_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class' : 'form-control'
        })
    )