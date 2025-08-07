
from django import template



from main.models import Category

register = template.Library()

menu=[
    {"name": "Main", "url":"main"},
    ]
@register.simple_tag
def get_menu():
    return menu

@register.simple_tag
def get_categories():
    return Category.objects.all()