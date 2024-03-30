from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from ..models import serviceStatus
from login.models import Admin
from ..forms import statusDetails
from ..models import serviceStatus
from ticketManagement.views import getUserType


class viewServiceStatus(DetailView):
    template_name = "viewServiceStatus.html"
    model = serviceStatus
    success_template_name = "successMessage.html"

    def get(self, request):
       
        username = request.session.get("user")

        services = self.model.objects.all()
    
        return render(request, self.template_name, {"userType": getUserType(username), "services" : services, "username" : username})