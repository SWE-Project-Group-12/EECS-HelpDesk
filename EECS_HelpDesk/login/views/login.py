from django.shortcuts import render


def login(request):
    """ Displays the login page if the user is not currently authenticated. """

    # If the request method is GET:
    # Check that the user is not authenticated.
    # If the user is already authenticated, redirect to a different URL.

    # If the request method is POST:
    # Take the details from the form and query the database.
    # If there are, redirect to a URL where authentication is required.
    # If there aren't, display an error message.

    return render(request, "login.html")
