from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # form.cleaned_data["username"]
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            return redirect("board:index")
    else:
        form = UserForm()
    return render(request, "users/register.html", {"form": form})
