from django.urls import path
from . import views

urlpatterns = [
    path("FAQs", views.FAQView.as_view(), name="FAQs"),
]