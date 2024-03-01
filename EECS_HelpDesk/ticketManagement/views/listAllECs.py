from django.shortcuts import render


def listAllECs(request):
    return render(request, "listAllECs.html")