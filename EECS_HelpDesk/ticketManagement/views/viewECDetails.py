from django.shortcuts import render


def viewECDetails(request, ticketID):
    """ View the details of a specified EC. """

    # Check if the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check if the user is of type EC Handler or is of type Admin or is of type Student.
    # If not, redirect to a page they're allowed to visit.
    # Get the EC from the database via the ticketID.
    # If the ticket is found, display the ticket.
    # If the ticket is not found, display an error message.

    return render(request, "viewECDetails.html")
