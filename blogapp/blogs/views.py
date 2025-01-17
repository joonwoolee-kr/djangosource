from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def blogs_list(request):
    # 작성일자 내림차순
    posts = Post.objects.all()
    return render(request, "blogs/list.html", {"posts": posts})


def blogs_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "blogs/detail.html", {"post": post})


@login_required(login_url="/users/login")
def blogs_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 작성자(== 로그인 사용자)
            post.user = request.user
            post.save()
            return redirect("blogs:list")
    else:
        form = PostForm()
    return render(request, "blogs/create.html", {"form": form})


@login_required(login_url="/users/login")
def blogs_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blogs:detail", pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blogs/update.html", {"form": form, "pk": pk})


@login_required(login_url="/users/login")
def blogs_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("blogs:list")


# @login_required: 로그인이 안 되어 있을 때 로그인 페이지로 이동
@login_required(login_url="users:login")
def comment_create(request):
    if request.method == "POST":
        content = request.POST.get("content").strip()
        post_pk = request.POST.get("post_pk").strip()
        # post = get_object_or_404(Post, pk=pk)
        post = get_object_or_404(Post, pk=post_pk)
        if content and post_pk:
            # Comment 생성
            # comment = Comment(post=post, user=request.user, content=content)
            # comment.save()
            comment = Comment.objects.create(
                post=post, user=request.user, content=content
            )
            return redirect("blogs:detail", pk=comment.post.pk)
    messages.error(request, "댓글을 입력해 주세요")
    return redirect("blogs:detail", pk=post_pk)
