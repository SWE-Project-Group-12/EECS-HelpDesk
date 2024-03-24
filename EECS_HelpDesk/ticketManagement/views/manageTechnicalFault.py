from ..models import TechnicalFault
from .manageTicket import manageTicket

class manageTechnicalFault(manageTicket):
    template_name = "manageTicket.html"
    model = TechnicalFault
    ticket_type = "Technical Fault"
    authorised_users = ["Admin", "Student", "TechnicalFaultHandler"]