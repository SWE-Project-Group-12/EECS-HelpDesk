from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from ticketManagement.views import getUserType
from ticketManagement.models import EC, TechnicalFault
from ..models import Student, ECHandler, TechnicalFaultHandler, Admin
from django.contrib import messages

class DeleteUserView(DeleteView):
    model = None

    def get(self, request, usernameToDelete, *args, **kwargs):
        username = request.session.get("user")

        if username is None:
            return HttpResponseRedirect("/login")
        elif len(Admin.objects.filter(pk=username)) != 1:
            return HttpResponseRedirect("/login")

        for UserModel in [Student, ECHandler, TechnicalFaultHandler, Admin]:
            user = UserModel.objects.filter(pk=usernameToDelete)
            if len(user) != 0:
                user.delete()
                EC.objects.filter(username=username).delete()
                TechnicalFault.objects.filter(username=username).delete()
                messages.success(request,"User Removed")
                return HttpResponseRedirect("/login")
            
        messages.error(request,"User Has Not Been Found.")

        return HttpResponseRedirect("/listAllUsers")