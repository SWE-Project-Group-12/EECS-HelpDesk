from django.shortcuts import render
from django.http import HttpResponseRedirect


def base(request):
    return HttpResponseRedirect("/login")