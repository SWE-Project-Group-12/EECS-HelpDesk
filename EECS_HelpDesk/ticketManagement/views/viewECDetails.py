from .viewTicketDetails import viewTicketDetails
from ..models import EC


class viewECDetails(viewTicketDetails):
    model = EC
    ticket_type = "EC"