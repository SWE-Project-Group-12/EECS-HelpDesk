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
        success = False

        # Validates the details
        if f.is_valid():
            cleaned_f = f.cleaned_data
            username = cleaned_f["username"]
            password = cleaned_f["password"]
            name = cleaned_f["name"]
            surname = cleaned_f["surname"]
            user_type = cleaned_f["user_type"]

            models_list = [Student, ECHandler, TechnicalFaultHandler, Admin]
            for userType in models_list:
                if user_type == userType.__name__:
                    if len(userType.objects.filter(pk=username)) == 1:
                        f.add_error("username", "Username already exists.")

                    else:
                        newUser = userType.objects.create(
                            name=name,
                            username=username,
                            surname=surname,
                            password=bcrypt.hashpw(str(password).encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                        )
                        newUser.save()
                        success = True

        if success:
            return render(request, self.success_template_name, {"username": request.session.get("user"), "userType": getUserType(request.session.get("user")), "message": USER_TYPES[user_type] + " Created."})


        return render(request, self.template_name, {"CreateUserForm": f, "userType": getUserType(request.session.get("user")), "username": request.session.get("user")})
