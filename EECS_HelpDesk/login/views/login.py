from django.shortcuts import render, redirect
from django.views import View
from ..forms import LoginForm 
from ..models import TechnicalFaultHandler, Student, ECHandler, Admin 


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
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = None

            for UserModel in [TechnicalFaultHandler, Student, ECHandler, Admin]:
                user = self.get_user(UserModel, username = username, password = password)
                if user is not None:
                    break

            if user is None:
                return render(request, "login.html", {'form': form, 'error_message': 'Invalid username or password.'})

            request.session['user'] = user.pk

            redirect_url = self.get_redirect_url(user)

            return redirect(redirect_url)

        return render(request, "login.html", {'form': form, 'error_message': 'Invalid username or password.'})
    
    def get_redirect_url(self, user):
        if isinstance(user, Student):
            username = user.username
            redirect_url = '/findPersonalTickets/{}'.format(str(username)) 
        else:
            redirect_url = '/listAllECs'
        
        return redirect_url

    def get_user(self, model, **kwargs):
        try:
            user = model.objects.get(**kwargs)
        except model.DoesNotExist:
            user = None
        return user
