from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    # 127.0.0.1:8000/blogs
    path("", blogs_list, name="list")
]
