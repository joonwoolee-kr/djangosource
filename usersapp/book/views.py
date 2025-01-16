from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Book
from .form import BookForm


class HomeView(TemplateView):
    template_name = "home.html"


def book_list(request):
    book_list = Book.objects.order_by("-id")
    return render(request, "books/list.html", {"book_list": book_list})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/detail.html", {"book": book})


def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:detail", book_id=book_id)
    else:
        form = BookForm(instance=book)

    return render(request, "books/edit.html", {"form": form, "book": book})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("books:detail", book_id=book.id)
    else:
        form = BookForm()

    return render(request, "books/create.html", {"form": form})


def book_remove(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("books:list")
