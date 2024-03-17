from django.urls import path
from . import views


urlpatterns = [
    path("", views.base, name="Base"),
    path("login", views.login.as_view(), name="Login"),
    path("createUser", views.createUser, name="Create New User"),
]