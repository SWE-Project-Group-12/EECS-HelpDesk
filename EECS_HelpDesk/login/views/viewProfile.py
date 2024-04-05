from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from login.models import Admin
from ..models import Student, ECHandler, TechnicalFaultHandler, Admin
from ..views import getUserType


class viewProfile(ListView):
    template_name = "viewProfile.html"

    def get(self, request):
       
        username = request.session.get("user")
        
        if username is None:
            return HttpResponseRedirect("/login")
        
        if getUserType(username) == "Student":
            userDetails = Student.objects.filter(username=username)
            
        elif getUserType(username) == "ECHandler":
            userDetails = ECHandler.objects.filter(username=username)
        
        elif getUserType(username) == "TechnicalFaultHandler":
            userDetails = TechnicalFaultHandler.objects.filter(username=username)
        elif getUserType(username) == "Admin":
            userDetails = Admin.objects.filter(username=username)
             
        else:
            return HttpResponseRedirect("/login")
        
    
        return render(request, self.template_name, {"userType": getUserType(username),"userDetails": userDetails  ,"username" : username})