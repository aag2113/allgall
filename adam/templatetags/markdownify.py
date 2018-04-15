from django import template

import mistune

register = template.Library()


@register.filter
def markdown(value):
    md = mistune.Markdown()
    return md.render(value)
