from django.db import models

# 모델(ORM - 클래스&테이블 1:1 매핑)
# 테이블명 지정하지 않으면 앱이름_모델명(ex - app1_person)
# 필드 지정
# 텍스트: CharField, TextField
# 숫자: IntegerField, SmallIntegerField, PositiveIntegerField...
# 날짜: DateTimefield, DateField, TimeField...
# 이메일: EmailField
# URL: URLField
# UUID: UUIDField
# IP: GenericIPAddressField
# 파일: FieldField, ImageField, FilePathField
# 참/거짓: BooleanField

# 관계: 외래키
# ManyToOne, OneToMany, OneToOne, ManyToMany

# 옵션
# blank, null, default, unique, choices, verbose_name, help_text, validators
# 날짜 타입 옵션
# auto_now_add: 처음에만 날짜/시간 삽입
# auto_now: save() 호출할 때 마다 날짜/시간 삽입(최종 수정 시간)


class Person(models.Model):
    # first_name = models.CharField(
    #     max_length=30,
    #     blank=True,
    #     null=True,
    #     verbose_name="이름1",
    #     unique=True,
    #     default="a",
    # )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.first_name}"


class Post(models.Model):
    """
    author_name, title, content, is_published(T/F), created_at, updated_at
    """

    author_name = models.CharField(max_length=20, verbose_name="작성자")
    title = models.CharField(max_length=100, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author_name}"
