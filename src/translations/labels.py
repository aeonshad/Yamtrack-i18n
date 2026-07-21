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
            "sort": {
                "date_added": _("Date Added"),
                "title": _("Title"),
                "media_type": _("Media Type"),
                "all_types": _("All Types"),
                "last_item_added": _("Last Item Added"),
                "name": _("Name"),
                "newest_first": _("Newest First"),
                "items_count": _("Items Count"),
            },
            "date_ranges": {
                "today": _("Today"),
                "yesterday": _("Yesterday"),
                "this_week": _("This Week"),
                "last_7_days": _("Last 7 Days"),
                "this_month": _("This Month"),
                "last_30_days": _("Last 30 Days"),
                "last_90_days": _("Last 90 Days"),
                "this_year": _("This Year"),
                "last_6_months": _("Last 6 Months"),
                "last_12_months": _("Last 12 Months"),
                "all_time": _("All Time"),
            },
            "chart_labels": {
                "count": _("Count"),
                "total": _("Total"),
                "score": _("Score"),
                "number_of_items": _("Number of Items"),
                "average_score": _("Average Score"),
                "item": _("item"),
                "items": _("items"),
                "statuses": {
                    "Completed": _("Completed"),
                    "In Progress": _("In Progress"),
                    "Planning": _("Planning"),
                    "Paused": _("Paused"),
                    "Dropped": _("Dropped"),
                },
            },
            "button": {
                "read_more": _("Read More"),
                "show_less": _("Show Less"),
                "show_failed_items": _("Show failed items"),
                "hide_failed_items": _("Hide failed items"),
                "show_traceback": _("Show traceback"),
                "hide_traceback": _("Hide traceback"),
            },
        }
    }