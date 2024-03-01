from django.shortcuts import render


def listAllTechnicalFaults(request):
    return render(request, "listAllTechnicalFaults.html")