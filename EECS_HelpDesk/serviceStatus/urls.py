from django.urls import path
from . import views

urlpatterns = [
    path("viewServiceStatus", views.viewServiceStatus.as_view(), name="viewServiceStatus"),
    path("editServiceStatus/<str:service_name>", views.editServiceStatus.as_view(), name="editServiceStatus"),
    
]