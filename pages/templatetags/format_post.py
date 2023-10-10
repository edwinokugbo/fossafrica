from django import template

register = template.Library()


@register.filter
def make_title(value):
    return value.replace(" ", "-").lower()


@register.filter
def nl2br(value):
    return value.replace("\n", "<br>").lower()
