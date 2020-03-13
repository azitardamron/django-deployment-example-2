from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all valyes of arg from string
    """
    return value.replace(arg,'')

# register.fitler('cut',cut)
