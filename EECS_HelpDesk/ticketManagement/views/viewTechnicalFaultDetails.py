from .viewTicketDetails import viewTicketDetails
from ..models import TechnicalFault


class viewTechnicalFaultDetails(viewTicketDetails):
    model = TechnicalFault
    ticket_type = "Technical Fault"