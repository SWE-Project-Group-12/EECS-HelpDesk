from django.shortcuts import render


def deleteTicket(request, ticketID):
    return render(request, "deleteTicket.html")
