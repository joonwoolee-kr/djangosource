from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm


def home(request):
    return render(request, "home.html")


def users_login(request):
    return render(request, "users/login.html")


def users_logout(request):
    logout(request)
    return redirect("users:home")


def users_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
