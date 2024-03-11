from django.forms import Form

class LoginForm:
    # Standard Form. Inherits from BaseUserDetails.
    # Used for logging in and authentication.
    class Meta:
        fields = ['username', 'password']