from django.urls import path
from . import views

urlpatterns = [
    path("createTicket/<str:username", views.createTicket, name="Create Ticket"),
    path("deleteTicket/<int:ticketID>", views.deleteTicket, name="Delete Ticket"),
    path("findPersonalTickets/<str:username>", views.findPersonalTickets, name="Find Personal Tickets"),
    path("viewStatus/<str:username>/<int:ticketID>", views.viewStatus, name="View Ticket Status"),
    path("listAllECs", views.listAllECs, name="List All ECs"),
    path("listAllTechnicalFaults", views.listAllTechnicalFaults, name="List All Technical Faults"),
    path("updateEC/<int:ticketID>", views.updateEC, name="Update EC"),
    path("updateTechnicalFault/<int:ticketID>", views.updateTechnicalFault, name="Update Technical Fault"),
    path("viewECDetails/<int:ticketID>", views.viewECDetails, name="View EC Details"),
    path("viewTechnicalFaultDetails/<int:ticketID>", views.viewTechnicalFaultDetails, name="View Technical Fault Details"),
]
