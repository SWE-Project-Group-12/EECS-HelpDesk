from .deleteTicket import DeleteTicketView
from ..models import TechnicalFault


class DeleteTechnicalFaultView(DeleteTicketView):
    model = TechnicalFault
    ticket_type = "Technical Fault"
