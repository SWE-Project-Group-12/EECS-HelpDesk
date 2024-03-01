from django.shortcuts import render


def createTicket(request, username):
    return render(request, "createTicket.html")
