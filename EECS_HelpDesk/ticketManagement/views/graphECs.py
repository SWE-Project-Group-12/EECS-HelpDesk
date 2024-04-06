from django.shortcuts import render
from ..models import EC
from .graphTickets import GraphTickets

"""def graphECs(request):

    pending = len(EC.objects.filter(status="Pending"))
    completed = len(EC.objects.all()) - pending

    return render(request, "t.html", {"completed": completed, "pending": pending})
    
    """


class GraphECs(GraphTickets):
    model = EC
    authorised_users = ["ECHandler", "Admin"]
    ticket_type = "EC"
    ticket_type_display = ticket_type