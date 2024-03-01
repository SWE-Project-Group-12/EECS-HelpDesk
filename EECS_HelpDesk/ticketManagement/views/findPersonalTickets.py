from django.shortcuts import render


def findPersonalTickets(request, username):
    return render(request, "findPersonalTickets.html")
