from django.shortcuts import render


def listAllTechnicalFaults(request):
    """ Displays all Technical Faults for Technical Fault Handlers and Admins. """

    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type Technical Fault Handler or is of type Admin.
    # If not, redirect to a page they're allowed to visit.
    # Get all Technical Faults from the database.

    return render(request, "listAllTechnicalFaults.html")
