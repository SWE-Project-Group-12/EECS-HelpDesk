from django.urls import path
from . import views

urlpatterns = [
    path("createEC/<str:username>", views.createEC.as_view(), name="Create Ticket"),
    path("createTechnicalFault/<str:username>", views.createTechnicalFault.as_view(), name="Create Technical Fault"),
    path("deleteEC/<str:username>/<int:ticketID>", views.DeleteECView.as_view(), name="Delete EC"),
    path("deleteTechnicalFault/<str:username>/<int:ticketID>", views.DeleteTechnicalFaultView.as_view(), name="Delete Technical Fault"),
    path("findPersonalTickets/<str:username>", views.FindPersonalTickets.as_view(), name="Find Personal Tickets"),
    path("listAllECs", views.ListAllECs.as_view(), name="List All ECs"),
    path("listAllTechnicalFaults", views.ListAllTechnicalFaults.as_view(), name="List All Technical Faults"),
    path("manageTechnicalFault/<int:ticketID>", views.manageTechnicalFault.as_view(), name="Manage Technical Fault"),
    path("manageEC/<int:ticketID>", views.manageEC.as_view(), name="Manage EC")
]
