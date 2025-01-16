from django.urls import path
from .views import *

app_name = "books"

urlpatterns = [
    # http://127.0.0.1:8000/books/ 전체도서목록(list)
    path("", book_list, name="list"),
    # http://127.0.0.1:8000/books/1 도서조회(detail)
    path("<int:book_id>/", book_detail, name="detail"),
    # http://127.0.0.1:8000/books/1/edit 도서수정(edit)
    path("<int:book_id>/edit/", book_edit, name="edit"),
    # http://127.0.0.1:8000/books/1/remove 도서삭제(remove)
    path("<int:book_id>/remove/", book_remove, name="remove"),
    # http://127.0.0.1:8000/books/1/create 도서추가(create)
    path("create/", book_create, name="create"),
]
