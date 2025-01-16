from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "users"
# http://127.0.0.1:8000/users/regsiter
urlpatterns = [
    path("register/", register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
