from django.shortcuts import render


def createUser(request):
    """ Displays the form to create a new user. Only Admins can access this page. """

    # If the request method is GET:
    # Check that the user is authenticated.
    # Check that the logged in user is of type Admin.

    # If the request method is POST:
    # Check that the user is authenticated and is of type Admin.
    # Validate the details in the form are correct. Validate names etc.
    # If valid, store the details and return a success message.
    # If invalid, return with an error message.

    return render(request, "createUser.html")