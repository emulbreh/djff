from django.template import Library
from djff.diff import UnifiedDiff

register = Library()

@register.filter
def udiff(diff):
    return UnifiedDiff(diff)
