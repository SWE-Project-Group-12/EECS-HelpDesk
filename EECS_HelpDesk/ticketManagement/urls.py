from django.urls import path
from . import views

urlpatterns = [
    # path("createEC/<str:username>", views.createEC, name="Create Ticket"),
    path("createEC/<str:username>", views.createEC.as_view(), name="Create Ticket"),
    # path("createTechnicalFault/<str:username>", views.createTechnicalFault, name="Create Technical Fault"),
    path("createTechnicalFault/<str:username>", views.createTechnicalFault.as_view(), name="Create Technical Fault"),
    path("deleteTicket/<str:username>/<int:ticketID>", views.deleteTicket, name="Delete Ticket"),
    path("findPersonalTickets/<str:username>", views.FindPersonalTickets.as_view(), name="Find Personal Tickets"),
    path("listAllECs", views.ListAllECs.as_view(), name="List All ECs"),
    path("listAllTechnicalFaults", views.ListAllTechnicalFaults.as_view(), name="List All Technical Faults"),
    path("updateEC/<int:ticketID>", views.updateEC, name="Update EC"),
    path("updateTechnicalFault/<int:ticketID>", views.updateTechnicalFault, name="Update Technical Fault"),
    path("viewECDetails/<int:ticketID>", views.viewECDetails, name="View EC Details"),
    path("viewTechnicalFaultDetails/<int:ticketID>", views.viewTechnicalFaultDetails, name="View Technical Fault Details"),
]
