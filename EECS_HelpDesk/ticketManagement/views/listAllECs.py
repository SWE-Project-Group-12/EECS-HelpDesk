from django.shortcuts import render


# def listAllECs(request):
#     """ Displays all ECs for EC Handlers and Admins to track and update. """

#     # Check if the user is authenticated.
#     # If the user is not authenticated, redirect to the login page.
#     # Check if the user is of type EC Handler or is of type Admin.
#     # If not, redirect to a page they're allowed to visit.
#     # Get all ECs from the database.

#     return render(request, "listAllECs.html")
#___________________________________________________________________________________________________

# class based view
# kwargs = keyword arguements dictionary that maps keywords names to corresponding values
# By using **kwargs, you can ensure that your view can accept any additional keyword arguments without causing an error.

from django.shortcuts import render, redirect
from django.apps import apps
from ticketManagement.models import EC
from django.views.generic import ListView

# Import the getUserType function
from . import getUserType

class ListAllECs(ListView):
    model = EC
    template_name = 'listAllECs.html'
    context_object_name = 'ec_list'

# dispatch method used when request made to a view
    def dispatch(self, request, *args, **kwargs):
        """
        Override the dispatch method to check if the user is authenticated and of type EC Handler or Admin.
        """

        # Check if the user is authenticated.
        if not getUserType(request.user.username):
            return redirect('login')

        # Check if the user is of type EC Handler or is of type Admin.
        if not (request.user.is_ec_handler or request.user.is_admin):
            return redirect('login')

        return super().dispatch(request, *args, **kwargs)

# method to filter objects based on view
    def get_queryset(self):
        """
        Override the get_queryset method to filter the ECs based on the user's permissions.
        """
        # Get all ECs from the database.
        queryset = super().get_queryset()
        if not self.request.user.is_ec_handler and not self.request.user.is_admin:
            queryset = queryset.filter(username=self.request.user)
        return queryset

# maps variable names to python objects
    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add the username variable to the context.
        """
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context