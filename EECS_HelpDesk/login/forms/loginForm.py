from django.forms import Form
from .baseUserDetails import BaseUserDetails

class LoginForm(BaseUserDetails):
    # Standard Form. Inherits from BaseUserDetails.
    # Used for logging in and authentication.
    class Meta:
        fields = ['username', 'password']
