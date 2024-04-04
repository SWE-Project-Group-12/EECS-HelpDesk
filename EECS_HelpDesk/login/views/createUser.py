from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from ..forms.createUserForm import CreateUserForm, USER_TYPES
from login.models import Admin, User, ECHandler, TechnicalFaultHandler, Student
from django.apps import apps
from .getUserType import getUserType
import bcrypt


class createUser(CreateView):
    """ Displays the form to create a new user. Only Admins can access this page. """
    template_name = 'createUser.html'
    success_template_name = "successMessage.html"
    success_url = '/listAllECs'

    # If the request method is GET:
    # Check that the user is authenticated.
    # Check that the logged in user is of type Admin.
    def get(self, request):
        username = request.session.get("user")

        if username is None:
            return HttpResponseRedirect("/login")
        elif len(Admin.objects.filter(pk=username)) != 1:
            return HttpResponseRedirect("/login")

        return render(request, "createUser.html", {"CreateUserForm": CreateUserForm, "userType": getUserType(username), "username": username})

    # If the request method is POST:
    # Check that the user is authenticated and is of type Admin.
    # Validate the details in the form are correct. Validate names etc.
    # If valid, store the details and return a success message.
    # If invalid, return with an error message.
    def post(self, request):

        username = request.session.get("user")
        if username is None:
            return HttpResponseRedirect("/login")
        elif len(Admin.objects.filter(pk=username)) != 1:
            return HttpResponseRedirect("/login")

        f = CreateUserForm(request.POST)
        success = True
        
        model = None
        models_list = [Student, ECHandler, TechnicalFaultHandler, Admin]

        # Validates the details
        if f.is_valid():
            cleaned_f = f.cleaned_data
            username = cleaned_f["username"]
            password = cleaned_f["password"]
            name = cleaned_f["name"]
            surname = cleaned_f["surname"]
            user_type = cleaned_f["user_type"]

            for letter in range(0, len(name)):
                if name[letter].isdigit():
                    f.add_error("name", "Please do not enter numbers in this field")
                    return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})
                    
            for letter in range(0, len(surname)):
                if surname[letter].isdigit():
                    f.add_error("surname", "Please do not enter numbers in this field")
                    return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})


            capital_letter = False
            number = False

            for letter in range(0, len(password_data)):
                if capital_letter and number:
                    break
                if password_data[letter].isupper():
                    capital_letter = True
                if password_data[letter].isdigit():
                    number = True

            if not capital_letter:
                f.add_error("password", "Password needs a captial letter")
                return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})

            
            if not number:
                f.add_error("password", "Password needs a number")
                return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})

            
            
            for userType in models_list:

                if len(userType.objects.filter(pk=username)) == 1:
                    success = False
                    f.add_error("username", "Username already exists.")
                    return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})


                if user_type == userType.__name__:
                    model = userType

        if not success:
            return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})

        newUser = model.objects.create(
            name=name,
            username=username,
            surname=surname,
            password=bcrypt.hashpw(str(password).encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        )
        newUser.save()

        return render(request, self.success_template_name, {"username": request.session.get("user"), "userType": getUserType(request.session.get("user")), "message": USER_TYPES[user_type] + " Created."})
