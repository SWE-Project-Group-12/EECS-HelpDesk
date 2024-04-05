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
from ticketManagement.models import EC, STATUS_CHOICES, PRIORITY_CHOICES
from ticketManagement.models import TechnicalFault
from login.models import Student
from .getUserType import getUserType
from django.http import HttpResponseRedirect
from .getFilteredTickets import getFilteredTickets


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

        statusFilters = list(request.GET.getlist("statusFilters")) if request.GET.get("statusFilters") is not None else STATUS_CHOICES.keys()
        priorityFilters = list(request.GET.getlist("priorityFilters")) if request.GET.get("priorityFilters") is not None else PRIORITY_CHOICES.keys()

        filters = []
        for x in statusFilters:
            for y in priorityFilters:
                filters.append({"status": x, "priority": y, "username": username})


        ECs = getFilteredTickets(EC, filters)
        techFault = getFilteredTickets(TechnicalFault, filters)

        return render(request, self.template_name, {"ECs" : ECs, "techFaults" : techFault, "username" : self.request.session.get("user"), "userType" : getUserType(username), "STATUS_CHOICES": STATUS_CHOICES, "PRIORITY_CHOICES": PRIORITY_CHOICES})