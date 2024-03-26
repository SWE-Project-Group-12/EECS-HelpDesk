from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from .getUserType import getUserType


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

        ticketID = kwargs['ticketID']
        self.model.objects.filter(pk=ticketID).delete()

        return render(request, self.template_name, {"username": username, "ticketType": self.ticket_type, "userType": getUserType(username), "message": self.ticket_type + " Removed."})
