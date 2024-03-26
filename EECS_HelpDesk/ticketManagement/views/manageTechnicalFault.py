from ..models import TechnicalFault
from .manageTicket import manageTicket

class manageTechnicalFault(manageTicket):
    template_name = "manageTechnicalFault.html"
    model = TechnicalFault
    ticket_type = "TechnicalFault"
    authorised_users = ["Admin", "TechnicalFaultHandler"]