from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from ..forms.createUserForm import CreateUserForm
from login.models import Admin, User, ECHandler, TechnicalFaultHandler, Student
from django.apps import apps
from .getUserType import getUserType


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

        return render(request, "createUser.html", {"CreateUserForm": CreateUserForm, "userType": getUserType(username)})

    # If the request method is POST:
    # Check that the user is authenticated and is of type Admin.
    # Validate the details in the form are correct. Validate names etc.
    # If valid, store the details and return a success message.
    # If invalid, return with an error message.
    def post(self, request):

        if username is None:
            return HttpResponseRedirect("/login")
        elif len(Admin.objects.filter(pk=username)) != 1:
            return HttpResponseRedirect("/login")

        f = CreateUserForm(request.POST)

        # Validates the details
        if f.is_valid():
            cleaned_f = f.cleaned_data
            username = cleaned_f["username"]
            password = cleaned_f["password"]
            name = cleaned_f["name"]
            surname = cleaned_f["surname"]
            user_type = cleaned_f["user_type"]

            success = False

            models_list = [Student, ECHandler, TechnicalFaultHandler, Student]
            for userType in models_list:
                if user_type == userType:
                    if len(userType.objects.filter(pk=username)) == 1:
                        f.add_error("username", "Username already exists,")

                    else:
                        success = True
                        userType.objects.create(
                            name=name,
                            username=username,
                            surname=surname,
                            password=password
                        )

        if success:
            return render(request, self.success_template_name, {"username": username, "ticketType": self.ticket_type, "userType": getUserType(username), "message": user_type + " Created."})

        else:
            return HttpResponseRedirect("/createUser")


        return render(request, self.template_name, {"CreateUserForm": CreateUserForm, "userType": getUserType(username)})





"""
            if user_type == "Student":
                if len(Student.objects.filter(pk=username)) == 1:
                    messages.add_message(request, messages.ERROR,
                                         'Username already exists')  # No need if we're going to do a success message template. Remove.
                else:
                    User = Student.objects.create(
                        name=name,
                        username=username,
                        surname=surname,
                        password=password
                    )
                    success = True
            elif user_type == "ECHandler":
                if len(ECHandler.objects.filter(pk=username)) == 1:
                    messages.add_message(request, messages.ERROR,
                                         'Username already exists')  # No need if we're going to do a success message template. Remove.
                else:
                    User = ECHandler.objects.create(
                        name=name,
                        username=username,
                        surname=surname,
                        password=password
                    )
                    success = True
            elif user_type == "TechHandler":
                if len(TechnicalFaultHandler.objects.filter(pk=username)) == 1:
                    messages.add_message(request, messages.ERROR,
                                         'Username already exists')  # No need if we're going to do a success message template. Remove.
                else:
                    User = TechnicalFaultHandler.objects.create(
                        name=name,
                        username=username,
                        surname=surname,
                        password=password
                    )
                    success = True
            elif user_type == "Admin":
                if len(Admin.objects.filter(pk=username)) == 1:
                    messages.add_message(request, messages.ERROR,
                                         'Username already exists')  # No need if we're going to do a success message template. Remove.
                else:
                    User = Admin.objects.create(
                        name=name,
                        username=username,
                        surname=surname,
                        password=password
                    )
                    success = True
                """