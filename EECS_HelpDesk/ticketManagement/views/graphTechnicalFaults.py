from django.shortcuts import render
from ..models import TechnicalFault
from .graphTickets import GraphTickets


"""
def graphTechnicalFaults(request):

    pending = len(TechnicalFault.objects.filter(status="Pending"))
    completed = len(TechnicalFault.objects.all()) - pending

    return render(request, "t.html", {"completed": completed, "pending": pending})

"""



class GraphTechnicalFaults(GraphTickets):
    model = TechnicalFault
    authorised_users = ["TechnicalFaultHandler", "Admin"]
    ticket_type = "TechnicalFault"