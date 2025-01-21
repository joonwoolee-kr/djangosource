from django.db import models
from django.contrib.auth.models import User

# 질문과 답변 게시판
# Question - pk(자동생성), 제목(subject), 내용(content), 작성일시(created_at), 수정일시(modified_at, null=True, blank=True)
# Answer - pk(자동생성), 질문(외래키), 내용, 작성일시, 수정일시


class Question(models.Model):
    subject = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="수정일시", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    # 추천
    voter = models.ManyToManyField(
        User, verbose_name="추천", related_name="voter_question"
    )

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(
        Question, verbose_name="질문", on_delete=models.CASCADE
    )
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="수정일시", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    # 추천
    voter = models.ManyToManyField(
        User, verbose_name="추천", related_name="voter_answer"
    )

    def __str__(self):
        return self.content


# 질문에 대한 댓글: author, content, created_at, modified_at, question
# 답변에 대한 댓글: author, content, created_at, modified_at, answer
class Comment(models.Model):
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="수정일시", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, verbose_name="질문", on_delete=models.CASCADE, null=True, blank=True
    )
    answer = models.ForeignKey(
        Answer, verbose_name="답변", on_delete=models.CASCADE, null=True, blank=True
    )
