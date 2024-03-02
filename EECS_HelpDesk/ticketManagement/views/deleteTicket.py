from django.shortcuts import render


def deleteTicket(request, username, ticketID):
    """ Deletes a ticket for a student. """

    # Check the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check the user is of type Student.
    # If the user is not of type Student, redirect to a page they're allowed to visit.
    # Check that the ticket is stored in the database (query via ticketID and username).
    # If the ticket is found, remove from the database and return a "ticket deleted" message.
    # If the ticket is not found, return an error message.

    return render(request, "deleteTicket.html")
