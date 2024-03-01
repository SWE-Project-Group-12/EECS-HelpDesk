from django.shortcuts import render


def updateEC(request, ticketID):
    return render(request, "updateEC.html")
