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

@register.filter
def translate_media_status(label_key):
    label_map = {
    "Completed": _("Completed"),
    "In Progress": _("In Progress"),
    "Planning": _("Planning"),
    "Paused": _("Paused"),
    "Dropped": _("Dropped"),
    }
    
    return label_map.get(
        label_key,
        label_key.replace("_", " ").title(),
    )
