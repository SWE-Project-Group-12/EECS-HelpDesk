from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.shortcuts import render
from ..forms import PasswordResetForm
from .getUserType import getUserType
import bcrypt
from login.models import Admin, User, ECHandler, TechnicalFaultHandler, Student


class ResetPasswordview(FormView):
    template_name = "resetPassword.html"
    success_template_name = "successMessage.html"
    form_class = PasswordResetForm

    def get(self, request, *args, **kwargs):

        username = request.session.get("user")
        if username is None:
            return HttpResponseRedirect("/login")

        form = self.form_class()

        return render(request, self.template_name, {'form': form, "username": username, "userType": getUserType(username), "name": request.session.get("name"), "surname": request.session.get("surname")})


    def post(self, request, *args, **kwargs):
        username = request.session.get("user")
        if username is None:
            return HttpResponseRedirect("/login")

        form = self.form_class(request.POST)
        if form.is_valid():
            for UserModel in [TechnicalFaultHandler, Student, ECHandler, Admin]:
                user = self.get_user(UserModel, username = username)
                if user is not None:
                    user.password = bcrypt.hashpw(str(form.cleaned_data['newPassword']).encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                    user.save()

            return render(request, self.success_template_name, {"username": username, "userType": getUserType(username), "message": "Password Changed.", "name": request.session.get("name"), "surname": request.session.get("surname")})

        return render(request, self.template_name, {'form': form, "username": username, "userType": getUserType(username), "name": request.session.get("name"), "surname": request.session.get("surname")})


    def get_user(self, model, **kwargs):
        try:
            user = model.objects.get(**kwargs)
        except model.DoesNotExist:
            user = None
        return user