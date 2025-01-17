from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    # 127.0.0.1:8000/blogs
    path("", blogs_list, name="list"),
    path("<int:pk>/", blogs_detail, name="detail"),
    path("create/", blogs_create, name="create"),
    path("<int:pk>/update/", blogs_update, name="update"),
    path("<int:pk>/delete/", blogs_delete, name="delete"),
    # path("<int:pk>/comment/create/", comment_create, name="create"),
    path("comment/create/", comment_create, name="comment_create"),
]
