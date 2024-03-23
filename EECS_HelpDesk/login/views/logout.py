from django.shortcuts import redirect
from django.views import View

class logout(View):

    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
        
        return redirect('Login')
