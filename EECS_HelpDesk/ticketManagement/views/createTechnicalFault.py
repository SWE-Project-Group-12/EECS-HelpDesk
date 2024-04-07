from django.shortcuts import render
from django.http import HttpResponseRedirect
from ticketManagement.forms import TechnicalFaultForm
from ticketManagement.models import TechnicalFault, LOCATION_CHOICES, PRIORITY_CHOICES
from login.models import Student
from django.views.generic.edit  import FormView
from .getUserType import getUserType
from django.contrib import messages

# def createTechnicalFault(request, username):
#     """ Displays the form to create a ticket for the student. """

#     # Note that this view is most likely to be split into "createEC" and "createTechnicalFault".

#     # If the request method is GET:
#     # Check the user is authenticated.
#     # If the user is not authenticated, redirect to the login page.
#     # Check the user is of type Student.
#     # If the user is not of type Student, redirect to a page they're allowed to visit.
#     # If authenticated and is of type Student, display the form.

#     # If the request method is POST:
#     # Check the user is authenticated.
#     # If the user is not authenticated, redirect to the login page.
#     # Check the user is of type Student.
#     # If the user is not of type Student, redirect to a page they're allowed to visit.
#     # If authenticated and is of type Student, validate the form.
#     # If the form is valid, store the ticket.
#     # If not valid, return with an error message.


#     if request.session.get("username") is None:
#         return HttpResponseRedirect("/login")


#     student = Student.objects.filter(username=username)

#     # validating to see if student exists in model
#     # comment the code below to see the actual page
#     if len(student) <= 0:
#         return HttpResponseRedirect("/listAllTechnicalFaults")

#     if request.method == "POST":
#         form = TechnicalFaultForm(request.POST)

#         if form.is_valid():
#             TechFault_ticket = TechnicalFault.objects.create(
#                 title = form.cleaned_data["title"],
#                 description = form.cleaned_data["description"],
#                 # status = form.cleaned_data["status"],             # pls look at baseTicketDetails for why i did this
#                 # dateCreated = form.cleaned_data["dateCreated"],   # pls look at baseTicketDetails for why i did this
#                 username = Student.objects.get(username=username),  # form says needs to be of Student instance
#                 location = form.cleaned_data['location']
#             )
#             TechFault_ticket.save()
#             return HttpResponseRedirect("/listAllTechnicalFaults")

#     else:
#         form = TechnicalFaultForm()

#     return render(request, "createTechnicalFault.html", {"form" : form})




# class based version
class createTechnicalFault(FormView):
    template_name = "createTechnicalFault.html"

    form_class = TechnicalFaultForm

    def get(self, request, username):
        form = self.form_class()

        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        
        if request.session.get("user") != username:
            return HttpResponseRedirect("/login")

        student = Student.objects.filter(username=username)

        # validating to see if student exists in model
        # comment the code below to see the actual page
        if len(student) <= 0:
            return HttpResponseRedirect("/listAllTechnicalFaults")

        return render(request, self.template_name, {"username": username, "form": form, "userType": getUserType(username), "name": request.session.get("name"), "surname": request.session.get("surname")})


    def post(self, request, username):
        form = self.form_class(request.POST, request.FILES)

        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        
        if request.session.get("user") != username:
            return HttpResponseRedirect("/login")

        student = Student.objects.filter(username=username)

        # validating to see if student exists in model
        # comment the code below to see the actual page
        if len(student) <= 0:
            return HttpResponseRedirect("/listAllTechnicalFaults")


        if form.is_valid():
            TechFault_ticket = TechnicalFault.objects.create(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                # status = form.cleaned_data["status"],             # pls look at baseTicketDetails for why i did this
                # dateCreated = form.cleaned_data["dateCreated"],   # pls look at baseTicketDetails for why i did this
                username = Student.objects.get(username=username),  # form says needs to be of Student instance
                location = form.cleaned_data['location'],
                priority = form.cleaned_data['priority'],
                evidence = form.cleaned_data['evidence'],
            )
            TechFault_ticket.save()
            message = "Technical Fault Saved."
            messages.success(request,message)
            
            return HttpResponseRedirect("/login")

        else:
            messages.error(request, "Form Error. Please Try Again.")
            return render(request, self.template_name, {"form" : form, "userType": getUserType(username), "username": username, "name": request.session.get("name"), "surname": request.session.get("surname")})

        return render(request, self.template_name, {"form" : form, "userType": getUserType(username), "username": username, "name": request.session.get("name"), "surname": request.session.get("surname")})
