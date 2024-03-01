from django.shortcuts import render
from django.http import HttpResponseRedirect


def base(request):
    return HttpResponseRedirect("/login")


def login(request):
    return render(request, "login.html")
