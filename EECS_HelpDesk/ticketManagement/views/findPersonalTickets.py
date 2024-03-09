from django.shortcuts import render


def findPersonalTickets(request, username):
    """ Returns a list of all the raised tickets by a Student """

    # Check the user is authenticated.
    # If the user is not authenticated, redirect to the login page.
    # Check the user is of type Student.
    # If the user is not of type Student, redirect to a page they're allowed to visit.
    # Query the database to find all the tickets for a student.

    return render(request, "findPersonalTickets.html")
