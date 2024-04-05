from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from login.models import Admin
from ..forms import CreateUserForm
from ..models import Student,ECHandler,Admin,TechnicalFaultHandler
from ticketManagement.views import getUserType
from django.contrib import messages

class manageUser(FormView):
    template_name = "manageUser.html"
    form_class = CreateUserForm

    def get(self, request,usernametomanage):
       
       
        username = request.session.get("user")
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        

        admin = Admin.objects.filter(username=username)

        # validating if the user accessing is an Admin
        if len(admin) <= 0:
            return HttpResponseRedirect("/login")
        usertomanage = None
        if getUserType(usernametomanage) == "Student":
            usertomanage = Student.objects.filter(username=usernametomanage).values()
            
            
        elif getUserType(usernametomanage) == "ECHandler":
            usertomanage = ECHandler.objects.filter(username=usernametomanage).values()
        
        elif getUserType(usernametomanage) == "TechnicalFaultHandler":
            usertomanage = TechnicalFaultHandler.objects.filter(username=usernametomanage).values()
        
        elif getUserType(usernametomanage) == "Admin":
            usertomanage = Admin.objects.filter(username=usernametomanage).values()
        else:
            messages.error(request, "Username has not been found")
            return HttpResponseRedirect("/listAllUsers")

        
        formdetails = [userdetails for userdetails in usertomanage]            
        formdetails[0]['user_type'] = getUserType(usernametomanage)
        form = self.form_class(formdetails[0])
        form.fields.get('username').widget.attrs['readonly'] = True

        return render(request, self.template_name, {"form": form, "userType": getUserType(username), "usernametomanage" : usernametomanage})

    def post(self, request, usernametomanage):
        form = self.form_class(request.POST)

        username = request.session.get("user")
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")

        admin = Admin.objects.filter(username=username)
        if len(admin) <= 0:
            return HttpResponseRedirect("/login")
        if form.is_valid():
            usertomanage = None
            if getUserType(usernametomanage) == "Student":
                usertomanage = Student.objects.get(username=usernametomanage)
                
            elif getUserType(usernametomanage) == "ECHandler":
                usertomanage = ECHandler.objects.get(username=usernametomanage)
            
            elif getUserType(usernametomanage) == "TechnicalFaultHandler":
                usertomanage = TechnicalFaultHandler.objects.get(username=usernametomanage)
            
            elif getUserType(usernametomanage) == "Admin":
                usertomanage = Admin.objects.get(username=usernametomanage)
            else:
                messages.error(request, "Username has not been found")
                return render(request, self.template_name, {"form" : form, "userType": getUserType(username)})
        
            

            usertomanage.name = form.cleaned_data["name"]
            usertomanage.surname = form.cleaned_data["surname"]

            # validating name and surname inputs 
            if any(chr.isdigit() for chr in form.cleaned_data["name"]):
                messages.error(request, "First name cannot contain numbers")
                return render(request, self.template_name, {"form" : form, "userType": getUserType(username)})

            if any(chr.isdigit() for chr in form.cleaned_data["surname"]):
                messages.error(request, "Surname cannot contain numbers")
                return render(request, self.template_name, {"form" : form, "userType": getUserType(username)})


            usertomanage.save()
            messages.success(request,"User Details Updated")
            return HttpResponseRedirect("/listAllUsers")

        return render(request, self.template_name, {"form" : form, "userType": getUserType(username)})
        