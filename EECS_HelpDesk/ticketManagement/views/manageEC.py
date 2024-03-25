from ..models import EC
from .manageTicket import manageTicket

class manageEC(manageTicket):
    template_name = "manageTicket.html"
    model = EC
    ticket_type = "EC"
    authorised_users = ["Admin", "Student", "ECHandler"]