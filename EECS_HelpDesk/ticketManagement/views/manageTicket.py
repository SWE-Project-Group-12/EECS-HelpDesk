from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .getUserType import getUserType


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
            

        return render(request, self.template_name , {"ticketDetails": ticketDetails, "ticketID" : ticketID, "userType" : getUserType})

    def post(self, request, *args, **kwargs):

        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        username = request.session.get("user")

        if getUserType not in self.authorised_users:
            return("/login")
        
        ticketID = kwargs["ticketID"]
        ticket = self.model.objects.filter(pk=ticketID)

        if len(ticket) != 1:
            return HttpResponseRedirect("/listAll" +self.ticket_type.replace(" ", "") + "s")
        status_decision = request.POST.get("status_decision")
        
        
        return render(request, self.template_name)




