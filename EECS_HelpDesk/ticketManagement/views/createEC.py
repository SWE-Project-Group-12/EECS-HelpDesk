from django.shortcuts import render
from django.http import HttpResponseRedirect
from ticketManagement.forms import ECForm
from ticketManagement.models import EC
from login.models import Student
from django.views.generic.edit  import FormView
from .getUserType import getUserType
from django.contrib import messages


# def createEC(request, username):
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
#         return HttpResponseRedirect("/listAllECs")

#     if request.method == "POST":
#         form = ECForm(request.POST)

#         if form.is_valid():
#             EC_ticket = EC.objects.create(
#                 title = form.cleaned_data["title"],
#                 description = form.cleaned_data["description"],
#                 # status = form.cleaned_data["status"],             # pls look at baseTicketDetails for why i did this
#                 # dateCreated = form.cleaned_data["dateCreated"],   # pls look at baseTicketDetails for why i did this
#                 username = Student.objects.get(username=username),  # form says needs to be of Student instance
#                 module = form.cleaned_data["module"],
#                 component = form.cleaned_data["component"]
#             )
#             EC_ticket.save()
#             return HttpResponseRedirect("/listAllECs")

#     else:
#         form = ECForm()

#     return render(request, "createEC.html", {"form" : form})




# class based version 
class createEC(FormView):
    template_name = "createEC.html"
    form_class = ECForm
    success_template_name = "successMessage.html"

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
            return HttpResponseRedirect("/listAllECs")

        return render(request, self.template_name, {"username": username,"form": form, "userType": getUserType(username)})

    def post(self, request, username):
        form = self.form_class(request.POST, request.FILES)

        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        
        if request.session.get("user") != username:
            return HttpResponseRedirect("/login")

        # validating to see if student exists in model
        # comment the code below to see the actual page
        student = Student.objects.filter(username=username)
        if len(student) <= 0:
            return HttpResponseRedirect("/listAllECs")

        if form.is_valid():
            EC_ticket = EC.objects.create(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                # status = form.cleaned_data["status"],             # pls look at baseTicketDetails for why i did this
                # dateCreated = form.cleaned_data["dateCreated"],   # pls look at baseTicketDetails for why i did this
                username = Student.objects.get(username=username),  # form says needs to be of Student instance
                module = form.cleaned_data["module"],
                component = form.cleaned_data["component"],
                priority = form.cleaned_data['priority'],
                evidence = form.cleaned_data['evidence'],
            )
            EC_ticket.save()

            message = "EC Saved."
            messages.success(request,message)
            
            return HttpResponseRedirect("/login")

        return render(request, self.template_name, {"form" : form, "userType": getUserType(username), "username": username})
        