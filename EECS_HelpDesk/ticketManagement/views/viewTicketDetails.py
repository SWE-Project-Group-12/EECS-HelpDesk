from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from .getUserType import getUserType


class viewTicketDetails(DetailView):
    model = None
    template_name = "viewTicketDetails.html"
    ticket_type = None
    

    def get(self, request, username, ticketID, *args, **kwargs):
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")

        if getUserType(request.session.get("user")) != "Student":
            return HttpResponseRedirect("/listAllECs")

        if request.session.get('user') != username:
            return HttpResponseRedirect("/findPersonalTickets/" + username)

        ticketDetails = [details for details in self.model.objects.filter(pk=ticketID).values()]

        if len(ticketDetails) <= 0:
            return render(request, "successMessage.html", {"username": username, "message": self.ticket_type + " with Ticket ID " + str(ticketID) + " has not been found."})

        return render(request, self.template_name, {"username": username, "userType": getUserType(username), "ticket": ticketDetails[0], "ticketType": self.ticket_type, "name": request.session.get("name"), "surname": request.session.get("surname")})