from django.shortcuts import render


def updateTechnicalFault(request, ticketID):
    """ Update the status of a specific EC. """

    # If the request method is GET:
    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type Technical Fault Handler or is of type Admin.
    # If not, redirect to a page they're allowed to visit.
    # Get the specific Technical Fault from the database.
    # Display the Technical Fault and add buttons to update the status.

    # If the request method is POST:
    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type Technical Fault Handler or is of type Admin.
    # If not, redirect to a page they're allowed to visit.
    # Check that received data includes a status update.
    # Store the status update for the Technical Fault in the database.

    return render(request, "updateTechnicalFault.html")
