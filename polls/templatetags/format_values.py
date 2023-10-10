from django import template

register = template.Library()


@register.simple_tag
def get_percentage(value, total_value):
    perc = (value / total_value) * 100
    return round(perc, 2)
