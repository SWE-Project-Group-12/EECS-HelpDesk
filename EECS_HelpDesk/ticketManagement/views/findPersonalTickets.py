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
from ticketManagement.models import Ticket
from . import getUserType

class FindPersonalTickets(ListView):
    model = Ticket
    template_name = 'findPersonalTickets.html'
    context_object_name = 'tickets'

    def dispatch(self, request, *args, **kwargs):
        """
        Override the dispatch method to check if the user is authenticated and of type Student.
        """

        # Check if the user is authenticated.
        if not request.user.is_authenticated:
            return redirect('login')

        # Check if the user is of type Student.
        if getUserType(request.user.username) != 'Student':
            return redirect('login')

        # Get the username from the URL.
        username = kwargs['username']

        # Check if the user is requesting their own tickets.
        if username != request.user.username:
            # redirects to login page but should be error page instead?
            return redirect('error_page')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Override the get_queryset method to filter the tickets based on the user's permissions.
        """
        # Get all tickets from the database.
        queryset = super().get_queryset()
        if getUserType(self.request.user.username) != 'Student':
            queryset = queryset.filter(username=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add the username variable to the context.
        """
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context