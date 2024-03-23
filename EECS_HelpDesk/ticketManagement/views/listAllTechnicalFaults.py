# from django.shortcuts import render

# def listAllTechnicalFaults(request):
#     """ Displays all Technical Faults for Technical Fault Handlers and Admins. """

#     # Check if the user is authenticated.
#     # If the user is not authenticated, redirect to the login page.
#     # Check if the user is of type Technical Fault Handler or is of type Admin.
#     # If not, redirect to a page they're allowed to visit.
#     # Get all Technical Faults from the database.

#     return render(request, "listAllTechnicalFaults.html")

#_________________________________________________________________________________________________________

from django.shortcuts import render, redirect
from django.views.generic import ListView
from ticketManagement.models import TechnicalFault
from . import getUserType

# Similar to the ListAllECs class, create a ListAllTechnicalFaults class
class ListAllTechnicalFaults(ListView):
    model = TechnicalFault
    template_name = 'listAllTechnicalFaults.html'
    context_object_name = 'technical_fault_list'

    def dispatch(self, request, *args, **kwargs):
        """
        Override the dispatch method to check if the user is authenticated and of type Technical Fault Handler or Admin.
        """

        # Check if the user is authenticated.
        if not getUserType(request.user.username):
            return redirect('login')

        # Check if the user is of type Technical Fault Handler or is of type Admin.
        if not (request.user.is_technical_fault_handler or request.user.is_admin):
            return redirect('login')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Override the get_queryset method to filter the Technical Faults based on the user's permissions.
        """
        # Get all Technical Faults from the database.
        queryset = super().get_queryset()
        if not self.request.user.is_technical_fault_handler and not self.request.user.is_admin:
            queryset = queryset.filter(username=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add the username variable to the context.
        """
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context