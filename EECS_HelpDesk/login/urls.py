from django.urls import path
from . import views


urlpatterns = [
    path("", views.base, name="Base"),
    path("login", views.login, name="Login"),
]