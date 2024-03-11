from django import forms
from .baseTicketDetails import BaseTicketDetails


class ECForm(BaseTicketDetails):
    # ModelForm. Based on the Model EC.
    # Inherits form headings from Base Ticket Details.
    # Used to validate ECs.
    
    module = forms.CharField(max_length=100, required=True)
    component = forms.CharField(max_length=100, required=True)