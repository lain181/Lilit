
from django import template

register = template.Library()

menu=[{"name": "About", "url":"about"},
    {"name": "Main", "url":"main"},
    {"name": "Popular", "url":"popular"},
    ]
@register.simple_tag
def get_menu():
    return menu