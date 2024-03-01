from django.shortcuts import render


def viewECDetails(request, ticketID):
    return render(request, "viewECDetails.html")