from django.urls import path
from .views import *

app_name = "board"

urlpatterns = [
    path("", index, name="index"),
    path("question/<int:id>/", detail, name="detail"),
    path("question/create/", create, name="create"),
    path("question/modify/<int:id>", modify, name="modify"),
    path("question/delete/<int:id>", delete, name="delete"),
    # 답변
    path("answer/create/<int:id>/", answer_create, name="answer_create"),
]
