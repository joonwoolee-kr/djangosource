from django.utils.safestring import mark_safe
import markdown
from django import template

register = template.Library()


@register.filter
def mark(value):
    # 확장도구 추가
    # nl2br: 줄바꿈, fenced_code: 마크다운 소스코드
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def index(value, arg):
    return ((value - 1) * 10) + arg
