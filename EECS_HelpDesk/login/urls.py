from django.urls import path
from . import views


urlpatterns = [
    path("", views.base, name="Base"),
    path("login", views.login.as_view(), name="Login"),
    path("createUser", views.createUser.as_view(), name="Create New User"),
    path("logout", views.logout.as_view(), name="Logout"),
    path("listAllUsers", views.listAllUsers.as_view(), name="listAllUsers"),
    path("manageUser/<str:usernametomanage>", views.manageUser.as_view(), name="manageUser"),
    path("resetPassword", views.ResetPasswordview.as_view(), name="ResetPasswordView"),
    path("deleteUser/<str:usernameToDelete>", views.DeleteUserView.as_view(), name="DeleteUser"),
]