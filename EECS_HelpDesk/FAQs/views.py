from django.shortcuts import render
from django.views.generic import ListView
from ticketManagement.views import getUserType
from .models import FAQ

class FAQView(ListView):
    template_name = "FAQs.html"
    model = FAQ

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"FAQs": self.model.objects.all(), "username": request.session.get("user"), "userType": getUserType(request.session.get("user"))})