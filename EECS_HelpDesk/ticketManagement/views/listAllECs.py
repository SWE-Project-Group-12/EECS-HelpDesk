from django.shortcuts import render


def listAllECs(request):
    """ Displays all ECs for EC Handlers and Admins to track and update. """

    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type EC Handler or is of type Admin.
    # If not, redirect to a page they're allowed to visit.
    # Get all ECs from the database.

    return render(request, "listAllECs.html")
