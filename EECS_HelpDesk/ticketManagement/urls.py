from django.urls import path
from . import views

urlpatterns = [
    path("createEC/<str:username>", views.createEC.as_view(), name="CreateEC"),
    path("createTechnicalFault/<str:username>", views.createTechnicalFault.as_view(), name="CreateTechnicalFault"),
    path("deleteEC/<str:username>/<int:ticketID>", views.DeleteECView.as_view(), name="DeleteEC"),
    path("deleteTechnicalFault/<str:username>/<int:ticketID>", views.DeleteTechnicalFaultView.as_view(), name="DeleteTechnicalFault"),
    path("findPersonalTickets/<str:username>", views.FindPersonalTickets.as_view(), name="FindPersonalTickets"),
    path("listAllECs", views.ListAllECs.as_view(), name="ListECs"),
    path("listAllTechnicalFaults", views.ListAllTechnicalFaults.as_view(), name="ListTechnicalFaults"),
    path("manageTechnicalFault/<int:ticketID>", views.manageTechnicalFault.as_view(), name="ManageTechnicalFault"),
    path("manageEC/<int:ticketID>", views.manageEC.as_view(), name="ManageEC"),
    path("viewECDetails/<str:username>/<int:ticketID>", views.viewECDetails.as_view(), name="ViewECDetails"),
    path("viewTechnicalFaultDetails/<str:username>/<int:ticketID>", views.viewTechnicalFaultDetails.as_view(), name="ViewTechnicalFaultDetails"),
    path("graphECs", views.GraphECs.as_view(), name = "Graph ECs"),
    path("graphTechnicalFaults", views.GraphTechnicalFaults.as_view(), name = "Graph Technical Faults"),
]
