from django.shortcuts import render


def updateEC(request, ticketID):
    """ Update the status of a specific EC. """

    # If the request method is GET:
    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type EC Handler or is of type Admin.
    # If not, redirect to a page they're allowed to visit.
    # Get the specific EC from the database.
    # Display the EC data and add buttons to update the status.

    # If the request method is POST:
    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type EC Handler or is of type Admin.
    # If not, redirect to a page they're allowed to visit.
    # Check that received data includes a status update.
    # Store the status update for the EC in the database.

    return render(request, "updateEC.html")
