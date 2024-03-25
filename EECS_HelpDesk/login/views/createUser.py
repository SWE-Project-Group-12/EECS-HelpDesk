from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from ..forms.createUserForm import CreateUserForm
from login.models import Admin, User, ECHandler, TechnicalFaultHandler, Student
from django.apps import apps
# from ...ticketManagement.views.getUserType import getUserType

class createUser(CreateView):
    """ Displays the form to create a new user. Only Admins can access this page. """
    template_name = 'createUser.html'
    success_url = '/listAllECs'

    # If the request method is GET:
    # Check that the user is authenticated.
    # Check that the logged in user is of type Admin.
    def get(self, request):
        username = request.session.get("user")
        print("Username!: ", username)

        if username is None:
            print("Not logged in")
            return HttpResponseRedirect("/login")
        elif len(Admin.objects.filter(pk=username)) == 1:
            print(Admin.__name__)
            return render(request, "createUser.html", {"CreateUserForm": CreateUserForm})
        else:
            # CHANGE THIS LATER :)
            print("Not an Admin, get out of here!")
            return HttpResponseRedirect("/login")

        return render(request, "createUser.html", {"CreateUserForm": CreateUserForm})

    # If the request method is POST:
    # Check that the user is authenticated and is of type Admin.
    # Validate the details in the form are correct. Validate names etc.
    # If valid, store the details and return a success message.
    # If invalid, return with an error message.
    def post(self, request):
        f = CreateUserForm(request.POST)

        # Validates the details
        if f.is_valid():
            print("Form cleaned data: ", f.cleaned_data)
            cleaned_f = f.cleaned_data
            username = cleaned_f["username"]
            password = cleaned_f["password"]
            name = cleaned_f["name"]
            surname = cleaned_f["surname"]
            user_type = cleaned_f["user_type"]

            print("POST REQUEST!")
            print(username)
            print(password)
            print(name)
            print(surname)
            print(user_type)

            success = False

            # Talk with group. Bad to hardcode, should use enums or maybe django has a feature?
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

            if success:
                return HttpResponseRedirect(self.success_url) # Redirected to "/listAllECs" but this needs to be a success message. Leave it for now.
            else:
                return HttpResponseRedirect("/createUser")
        else:
            messages.add_message(request, messages.ERROR, 'User Creation Unsuccessful') # No need if we're going to do a success message template. Remove.

        return render(request, self.template_name, {"CreateUserForm": CreateUserForm})


