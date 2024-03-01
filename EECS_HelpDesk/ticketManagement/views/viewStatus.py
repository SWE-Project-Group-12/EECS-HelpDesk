from django.shortcuts import render


def viewStatus(request, username, ticketID):
    return render(request, "viewTicketStatus.html")
