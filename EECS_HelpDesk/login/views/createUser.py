from django.shortcuts import render


def createUser(request):
    return render(request, "createUser.html")