from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()

@register.filter
def translate_home_sort(label_key):
    label_map = {
    "Upcoming": _("Upcoming"),
    "Recent": _("Recent"),
    "Completion": _("Completion"),
    "Episodes Left": _("Episodes Left"),
    "Title": _("Title"),
    }

    return label_map.get(
        label_key,
        label_key.replace("_", " ").title(),
    )
