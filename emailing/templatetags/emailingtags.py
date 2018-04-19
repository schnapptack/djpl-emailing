from __future__ import unicode_literals
from django import template
from django.template.loader import get_template

register = template.Library()

@register.tag
def content_section(parser, token):
    nodelist = parser.parse(('end_content_section',))
    parser.delete_first_token()
    return UpperNode(nodelist)

class UpperNode(template.Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        inner_html = self.nodelist.render(context)
        return get_template('emailing/content_section.html').render(dict(inner_html=inner_html))



@register.simple_tag
def br():
    """
    Linebreak in email links mailto:?body=...
    """
    return '%0D%0A'

@register.simple_tag
def space():
    """
    Space in email links mailto:?body=...
    """
    return '%20'