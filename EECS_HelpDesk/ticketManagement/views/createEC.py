from django.shortcuts import render


def createEC(request, username):
    """ Displays the form to create a ticket for the student. """

    # Note that this view is most likely to be split into "createEC" and "createTechnicalFault".

    # If the request method is GET:
    # Check the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check the user is of type Student.
    # If the user is not of type Student, redirect to a page they're allowed to visit.
    # If authenticated and is of type Student, display the form.

    # If the request method is POST:
    # Check the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check the user is of type Student.
    # If the user is not of type Student, redirect to a page they're allowed to visit.
    # If authenticated and is of type Student, validate the form.
    # If the form is valid, store the ticket.
    # If not valid, return with an error message.

    return render(request, "createEC.html")
