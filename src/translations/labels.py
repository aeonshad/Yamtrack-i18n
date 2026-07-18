from django.utils.translation import gettext_lazy as _


def ui_labels(request):
    return {
        "ui_labels": {
            "import": {
                "once": {
                    "yamtrack": _("Import from YamTrack backup"),
                    "games": _("Import games"),
                    "media": _("Import movies and TV shows from your ratings"),
                    "books": _("Import from GoodReads backup"),
                },
                "periodic": _("File uploads are not available for periodic imports"),
            },
        }
    }