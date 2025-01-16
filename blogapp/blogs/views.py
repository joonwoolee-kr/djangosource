from django.shortcuts import render, redirect
from .models import *


def blogs_list(request):
    # 작성일자 내림차순
    posts = Post.objects.all()
    return render(request, "blogs/list.html", {"posts": posts})
