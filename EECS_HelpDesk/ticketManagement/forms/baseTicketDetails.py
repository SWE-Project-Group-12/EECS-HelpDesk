from django import forms


class BaseTicketDetails(forms.Form):
    # Abstract Form (Similar to abstract models, see https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the common form headings for an EC Form and Technical Fault Form.

    STATUS_CHOICES = {
		"UPDATED" : "Updated",
		"VOID" : "Void",
        "PENDING" : "Pending",
	}

    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea)

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        disabled=True,
        widget=forms.Select(attrs={
            'class' : 'form-control'
        })
    )

    dateCreated = forms.DateField(disabled=True)
    # username not sure what to do here because this is a foreign key field

    class Meta: 
        abstract = True