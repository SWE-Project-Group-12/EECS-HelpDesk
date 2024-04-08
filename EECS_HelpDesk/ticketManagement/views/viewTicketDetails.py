from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from .getUserType import getUserType
from datetime import datetime
import re
from django.contrib import messages


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
            messages.error(request,self.ticket_type + " with Ticket ID " + str(ticketID) + " has not been found.")
            return HttpResponseRedirect("/findPersonalTickets/" + username)

        ticketDetails = ticketDetails[0]

        if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", ticketDetails['dateResolved']):
            year = ticketDetails['dateResolved'].split("-")[0]
            month = ticketDetails['dateResolved'].split("-")[1]
            day = ticketDetails['dateResolved'].split("-")[2]
            ticketDetails['dateResolved'] = datetime(int(year), int(month), int(day)).strftime("%b %d, %Y")

        return render(request, self.template_name, {"username": username, "userType": getUserType(username), "ticket": ticketDetails, "ticketType": self.ticket_type, "name": request.session.get("name"), "surname": request.session.get("surname")})