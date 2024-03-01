from django.shortcuts import render


def viewTechnicalFaultDetails(request, ticketID):
    return render(request, "viewTechnicalFaultDetails.html")