from django.shortcuts import render
from django.http import HttpResponseRedirect


def base(request):
    """ Redirects straight to login page. """
    return HttpResponseRedirect("/login")
