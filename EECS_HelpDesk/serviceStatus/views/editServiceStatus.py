from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from ..models import serviceStatus
from login.models import Admin
from ..forms import statusDetails
from ..models import serviceStatus
from ticketManagement.views import getUserType


class editServiceStatus(FormView):
    template_name = "editServiceStatus.html"
    form_class = statusDetails
    success_template_name = "successMessage.html"

    def get(self, request,service_name):
       
        form = self.form_class()
        username = request.session.get("user")
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        

        admin = Admin.objects.filter(username=username)

        # validating if the user accessing is an Admin
        if len(admin) <= 0:
            return HttpResponseRedirect("/login")
        
        service = serviceStatus.objects.filter(service_name=service_name)
        if len(service) <=0:
            return HttpResponseRedirect("/login")
    
        return render(request, self.template_name, {"form": form, "userType": getUserType(username), "service_name" : service_name})

    def post(self, request, service_name):
        form = self.form_class(request.POST)

        username = request.session.get("user")
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")

        admin = Admin.objects.filter(username=username)
        if len(admin) <= 0:
            return HttpResponseRedirect("/login")

        if form.is_valid():
            service = serviceStatus.objects.get(pk=service_name)
            service.status = form.cleaned_data["status"]
            service.status_description = form.cleaned_data["status_description"]
            service.save()

            return render(request, self.success_template_name, {"username": username, "userType": getUserType(username), "message": "Service Status Saved."})

        return render(request, self.template_name, {"form" : form, "userType": getUserType(username)})
        