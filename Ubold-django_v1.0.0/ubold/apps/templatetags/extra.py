from django import template

register = template.Library()

@register.simple_tag()
def multiply(op1, op2, *args, **kwargs):
    return round(op1 * op2, 2)