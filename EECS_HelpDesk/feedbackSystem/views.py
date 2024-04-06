from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import FormView
from login.models import Student
from login.views import getUserType


class FeedbackEntryView(FormView):
    template_name = "feedbackEntry.html"
    success_template_name = "successMessage.html"
    model = Feedback
    form_class = FeedbackForm

    def get(self, request, username, *args, **kwargs):
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        
        if request.session.get("user") != username:
            return HttpResponseRedirect("/login")

        student = Student.objects.filter(username=username)

        if len(student) <= 0:
            return HttpResponseRedirect("/login")


        form = self.form_class()

        return render(request, self.template_name, {"form": form, "username": username, "userType": getUserType(username), "name": request.session.get("name"), "surname": request.session.get("surname")})

    def post(self, request, username, *args, **kwargs):
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")
        
        if request.session.get("user") != username:
            return HttpResponseRedirect("/login")

        student = Student.objects.filter(username=username)

        if len(student) <= 0:
            return HttpResponseRedirect("/login")

        form = self.form_class(request.POST)
        if form.is_valid():
            newFeedback = Feedback.objects.create(feature=form.cleaned_data['feature'], rating=form.cleaned_data['rating'], description=form.cleaned_data['description'], username=Student.objects.get(pk=username))
            newFeedback.save()
            return render(request, self.success_template_name, {"username": username, "userType": getUserType(username), "message": "Feedback Saved.", "name": request.session.get("name"), "surname": request.session.get("surname")})

        return render(request, self.template_name, {"form": form, "username": username, "userType": getUserType(username), "name": request.session.get("name"), "surname": request.session.get("surname")})
