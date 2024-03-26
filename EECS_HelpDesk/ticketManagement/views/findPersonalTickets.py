# from django.shortcuts import render


# def findPersonalTickets(request, username):
#     """ Returns a list of all the raised tickets by a Student """

#     # Check the user is authenticated.
#     # If the user is not authenticated, redirect to the login page.
#     # Check the user is of type Student.
#     # If the user is not of type Student, redirect to a page they're allowed to visit.
#     # Query the database to find all the tickets for a student.

#     return render(request, "findPersonalTickets.html")

#______________________________________________________________________________________________________

from django.shortcuts import render, redirect
from django.views.generic import ListView
from ticketManagement.models import EC
from ticketManagement.models import TechnicalFault
from login.models import Student
from .getUserType import getUserType
from django.http import HttpResponseRedirect


class FindPersonalTickets(ListView):
    template_name = 'findPersonalTickets.html'
    context_object_name = 'tickets'
    
    def get(self, request, username):

        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        
        if request.session.get("user") != username:
            return HttpResponseRedirect("/login")

        student = Student.objects.filter(username=username)

        # validating to see if student exists in model
        # comment the code below to see the actual page
        if len(student) <= 0:
            return HttpResponseRedirect("/login")

        ECs = EC.objects.filter(username=username)
        techFault = TechnicalFault.objects.filter(username=username)

        return render(request, self.template_name, {"ECs" : ECs, "techFaults" : techFault, "username" : self.request.session.get("user"), "userType" : getUserType(username)})