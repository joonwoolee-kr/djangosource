from django.contrib import admin
from .models import Person, Post, Comment

# admin 사이트에서 관리할 모델 등록
# 1) admin.site.register(모델명) - 세부 지정 불가
admin.site.register(Person)


# 2)
# class PostAdmin(admin.ModelAdmin):
#     """
#     세부 지정
#     """
#     pass
# admin.site.register(Post)


# 3) 2)번 개선
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 기본은 __str__ 기준으로 admin 페이지에서 보여짐
    # list_display 지정 시 __str__ 무시됨
    list_display = ("title", "author_name", "is_published", "created_at")
    # 조회 시 링크 걸 컬럼 변경
    list_display_links = ("author_name",)
    # 검색창 생성
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "created_at")
    list_display_links = ("message",)
