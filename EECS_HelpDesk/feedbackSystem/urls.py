from django.urls import path
from . import views


urlpatterns = [
    path("feedbackEntry/<str:username>", views.FeedbackEntryView.as_view(), name="FeedbackEntry"),
]