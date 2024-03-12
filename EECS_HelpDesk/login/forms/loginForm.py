from django.forms import Form
import baseUserDetails

class LoginForm(baseUserDetails):
    # Standard Form. Inherits from BaseUserDetails.
    # Used for logging in and authentication.
    class Meta:
        fields = ['username', 'password']