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

    # def dispatch(self, request, *args, **kwargs):
    #     """
    #     Override the dispatch method to check if the user is authenticated and of type Student.
    #     """
    #     # Check if the user is authenticated.
    #     if request.session.get("user") is None:
    #         return redirect('/login')

    #     # Check if the user is of type Student.
    #     if getUserType(request.session.get("user")) != 'Student':
    #         return redirect('/login')

    #     # Get the username from the URL.
    #     username = kwargs['username']

    #     # Check if the user is requesting their own tickets.
    #     if username != request.session.get("user"):
    #         return redirect('/login')

    #     return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     """
    #     Override the get_queryset method to filter the tickets based on the user's permissions.
    #     """
    #     # Get all tickets from the database.
    #     queryset = super().get_queryset()
    #     if getUserType(self.request.session.get("user")) != 'Student':
    #         queryset = queryset.filter(pk=self.request.session.get("user"))
    #     return queryset

    # # def get_context_data(self, **kwargs):
    # #     """
    # #     Override the get_context_data method to add the username variable to the context.
    # #     """
    # #     context = super().get_context_data(**kwargs)
    # #     context['username'] = self.request.session.get("user")
    # #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['username'] = self.request.session.get("user")

    #     context['tickets'] = [
    #         {
    #             'title': ticket.title,
    #             'description': ticket.description,
    #             'status': ticket.status,
    #             'dateCreated': ticket.dateCreated,
    #         } for ticket in context['tickets']
    #     ]

    #     return context

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

        return render(request, self.template_name, {"ECs" : ECs, "techFaults" : techFault, "username" : self.request.session.get("user"), "userType" : getUserType})