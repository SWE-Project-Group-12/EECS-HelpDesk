from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from .getUserType import getUserType
from django.contrib import messages


class DeleteTicketView(DeleteView):
    template_name = "successMessage.html"
    model = None
    ticket_type = None

    def get(self, request, *args, **kwargs):
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")

        username = request.session.get("user")
        if getUserType(username) != "Student":
            return HttpResponseRedirect("/login")

        if username != kwargs['username']:
            return HttpResponseRedirect("/findPersonalTickets/" + username)

        message = self.ticket_type + " Deleted."

        ticketID = kwargs['ticketID']
        if len(self.model.objects.filter(pk=ticketID)) <= 0:
            message = self.ticket_type + " with ID " + str(ticketID) + " was not found."
            message.error(request, message)
            return HttpResponseRedirect("/findPersonalTickets/" + username)
        else:
            self.model.objects.filter(pk=ticketID).delete()
            message = self.ticket_type + " with ID " + str(ticketID) + " Deleted."
            messages.success(request,message)

        return HttpResponseRedirect("/login")
