from django.shortcuts import render, redirect
from django.views import View
from ..forms import LoginForm 
from ..models import TechnicalFaultHandler, Student, ECHandler, Admin
import bcrypt
from django.contrib import messages

class login(View):

    def get(self, request):
        if 'user' in request.session:

            pk = request.session['user']

            for UserModel in [TechnicalFaultHandler, Student, ECHandler, Admin]:
                    user = self.get_user(UserModel, pk = pk)
                    if user is not None:
                        break

            redirect_url = self.get_redirect_url(user)

            return redirect(redirect_url)

        form = LoginForm()
        return render(request, "login.html", {'form': form})

    def post(self, request):
        if 'user' in request.session:

            pk = request.session['user']

            for UserModel in [TechnicalFaultHandler, Student, ECHandler, Admin]:
                    user = self.get_user(UserModel, pk = pk)
                    if user is not None:
                        break

            redirect_url = self.get_redirect_url(user)

            return redirect(redirect_url)

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = None
            success = False

            for UserModel in [TechnicalFaultHandler, Student, ECHandler, Admin]:
                if self.get_user(UserModel, username = username) is not None:
                    user = self.get_user(UserModel, username = username)
                    if bcrypt.checkpw(password.encode("utf-8"), str(user.password).encode("utf-8")):
                        success = True

            if success:
                request.session['user'] = user.pk
                request.session['name'] = user.name
                request.session['surname'] = user.surname
                redirect_url = self.get_redirect_url(user)
                return redirect(redirect_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is invalid.")

        return render(request, "login.html", {'form': form})
    
    def get_redirect_url(self, user):
        if isinstance(user, Student):
            username = user.username
            redirect_url = '/findPersonalTickets/{}'.format(str(username)) 

        elif isinstance(user, TechnicalFaultHandler):
            username = user.username
            redirect_url = '/listAllTechnicalFaults'
        else:
            redirect_url = '/listAllECs'
        
        return redirect_url

    def get_user(self, model, **kwargs):
        try:
            user = model.objects.get(**kwargs)
        except model.DoesNotExist:
            user = None
        return user
