from .deleteTicket import DeleteTicketView
from ..models import EC


class DeleteECView(DeleteTicketView):
    model = EC
    ticket_type = "EC"
