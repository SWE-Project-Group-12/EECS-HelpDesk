from django.shortcuts import render


def updateTechnicalFault(request, ticketID):
    return render(request, "updateTechnicalFault.html")