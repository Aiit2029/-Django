from django import template

from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def oo(v1, v2):

    return v1 + v2 + '又幸福了哥'


@register.inclusion_tag('inclusiontags.html')
def func():

    return {'data':{11,22,333}}

