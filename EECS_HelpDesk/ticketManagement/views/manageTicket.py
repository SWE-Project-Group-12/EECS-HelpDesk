from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .getUserType import getUserType
from ..models import STATUS_CHOICES
from django.contrib import messages
from datetime import datetime

class manageTicket(View):
    template_name="manageTicket.html"
    model = None
    ticket_type = None
    authorised_users = []

    def get(self, request, *args, **kwargs):
        #gets the Ticket details for a given ticket and displays them.
        if request.session.get("user") is None: #checks if user is logged in.
            return HttpResponseRedirect("/login")
        username =  request.session.get("user")

        if getUserType(username) not in self.authorised_users: #Checks if the usertype of the user is in authorised_users.
            #If the user type is not in authorised user, the user is redirected url route they can access.
            if getUserType(username) == "Student":
                return HttpResponseRedirect("/findPersonalTickets/"+ username)
            
            elif getUserType(username) == "ECHandler":
                return HttpResponseRedirect("/listAllECs")
            
            elif getUserType(username) == "TechnicalFaultHandler":
                return HttpResponseRedirect("/listAllTechnicalFaults")
    
        ticketID = kwargs["ticketID"] #sets ticketID to the ticketID value passed as an argument
        ticketDetails = self.model.objects.filter(pk=ticketID).values() #gets the ticket details for the ticket with the ticketID from above

        if len(ticketDetails) <= 0:
            message = self.ticket_type + " with Ticket ID " + str(ticketID) + " does not exist."
            messages.error(request, message)
            return HttpResponseRedirect("/login")
            

        return render(request, self.template_name , {"ticketDetails": ticketDetails, "ticketID" : ticketID, "userType" : getUserType(username), "STATUS_CHOICES" : STATUS_CHOICES.keys(), "username": username, "name": request.session.get("name"), "surname": request.session.get("surname")})

    def post(self, request, *args, **kwargs):

        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        username = request.session.get("user")

        if getUserType(username) not in self.authorised_users:
            return("/login")
        
        ticketID = kwargs["ticketID"]
        ticket = self.model.objects.filter(pk=ticketID)

        if len(ticket) != 1:
            return HttpResponseRedirect("/listAll" +self.ticket_type.replace(" ", "") + "s")
        status_decision = request.POST.get("status_decision","")
        if status_decision not in STATUS_CHOICES:
            return HttpResponseRedirect("/manage"+ self.ticket_type + "/"+ str(ticketID))
        ticket = self.model.objects.get(pk=ticketID)
        ticket.status = status_decision
        ticket.status_update_reason = request.POST.get("reason", "")
        ticket.dateResolved = datetime.now().strftime("%Y-%m-%d")
        ticket.save()
        message = "Ticket ID: " + str(ticketID) + " Updated Successfully" 
        messages.success(request,message)
        
        return HttpResponseRedirect("/login")
