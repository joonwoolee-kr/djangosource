from django.db import models
from users.models import User


# 번호(자동생성), user, 제목(title), 내용(content), 이미지(image) - option, 작성날짜(created_at), 수정날짜(modified_at)
class Post(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    # /media/image 사용
    image = models.ImageField(
        verbose_name="첨부파일", blank=True, null=True, upload_to="image"
    )
    created_at = models.DateTimeField(verbose_name="작성날짜", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="수정날짜", auto_now=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    def __str__(self):
        return self.title


# 원본글, 작성자, 내용, 작성날짜, 수정날짜
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="원본글", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="작성날짜", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="수정날짜", auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.user}"
