from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from login.models import Admin
from ..models import Student, ECHandler, TechnicalFaultHandler, Admin
from ticketManagement.views import getUserType


class listAllUsers(ListView):
    template_name = "listAllUsers.html"

    def get(self, request):
       
        username = request.session.get("user")

        if username is None:
            return HttpResponseRedirect("/login")
        elif len(Admin.objects.filter(pk=username)) != 1:
            return HttpResponseRedirect("/login")
        
        students = Student.objects.all()
        admins = Admin.objects.all()
        echandlers = ECHandler.objects.all()
        technicalfaulthandlers = TechnicalFaultHandler.objects.all()
    
        return render(request, self.template_name, {"userType": getUserType(username), "students" : students,"admins": admins,"echandlers":echandlers, "technicalfaulthandlers":technicalfaulthandlers, "username" : username, "name": request.session.get("name"), "surname": request.session.get("surname")})