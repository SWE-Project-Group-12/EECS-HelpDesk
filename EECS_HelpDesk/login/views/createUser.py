from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from ..forms.createUserForm import CreateUserForm, USER_TYPES
from login.models import Admin, User, ECHandler, TechnicalFaultHandler, Student
from django.apps import apps
from .getUserType import getUserType
import bcrypt
from django.contrib import messages


class createUser(CreateView):
    """ Displays the form to create a new user. Only Admins can access this page. """
    template_name = 'createUser.html'
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

        return render(request, "createUser.html", {"CreateUserForm": CreateUserForm, "userType": getUserType(username), "username": username, "name": request.session.get("name"), "surname": request.session.get("surname")})

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
                    messages.error(request, "First name cannot contain numbers")
                    return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user"), "name": request.session.get("name"), "surname": request.session.get("surname")})
                    
            for letter in range(0, len(surname)):
                if surname[letter].isdigit():
                    messages.error(request, "Surname cannot contain numbers")
                    return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user"), "name": request.session.get("name"), "surname": request.session.get("surname")})


            capital_letter = False
            number = False

            for letter in range(0, len(password)):
                if capital_letter and number:
                    break
                if password[letter].isupper():
                    capital_letter = True
                if password[letter].isdigit():
                    number = True

            if not capital_letter:
                messages.error(request, "Password needs a captial letter")
                return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user"), "name": request.session.get("name"), "surname": request.session.get("surname")})

            
            if not number:
                messages.error(request, "Password needs a number")
                return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user"), "name": request.session.get("name"), "surname": request.session.get("surname")})

            
            
            for userType in models_list:

                if len(userType.objects.filter(pk=username)) == 1:
                    success = False
                    messages.error(request, "Username already exists.")
                    return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user"), "name": request.session.get("name"), "surname": request.session.get("surname")})


                if user_type == userType.__name__:
                    model = userType

        else:
            success = False

        if not success:
            messages.error(request, "Invalid Details. Please Try Again.")
            return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user"), "name": request.session.get("name"), "surname": request.session.get("surname")})

        newUser = model.objects.create(
            name=name,
            username=username,
            surname=surname,
            password=bcrypt.hashpw(str(password).encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        )
        newUser.save()
        message = USER_TYPES[user_type] + " Created."
        messages.success(request, message)

        return HttpResponseRedirect("/listAllUsers")
