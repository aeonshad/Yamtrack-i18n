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

@register.filter
def translate_media_details(label_key):
    label_map = {
    "year": _("Year"),
    "players": _("Players"),
    "playtime": _("Play Time"),
    "min_age": _("Minimum Age"),
    "designers": _("Designers"),
    "publishers": _("Publishers"),
    "publisher": _("Publisher"),
    "authors": _("Authors"),
    "author": _("Author"),
    "start_date": _("Start Date"),
    "end_date": _("End Date"),
    "release_date": _("Release Date"),
    "publish_date": _("Publish Date"),
    "first_air_date": _("First Air Date"),
    "last_air_date": _("Last Air Date"),
    "format": _("Format"),
    "status": _("Status"),
    "runtime": _("Runtime"),
    "total_runtime": _("Total Runtime"),
    "episodes": _("Episodes"),
    "seasons": _("Seasons"),
    "season": _("Season"),
    "number_of_pages": _("Number of Pages"),
    "number_of_chapters": _("Number of Chapters"),
    "issues_count": _("Issues Count"),
    "last_issue_name": _("Last Issue Name"),
    "last_issue_number": _("Last Issue Number"),
    "latest_chapter_translated": _("Latest Translated Chapter"),
    "studios": _("Studios"),
    "companies": _("Companies"),
    "designers": _("Designers"),
    "themes": _("Themes"),
    "platforms": _("Platforms"),
    "country": _("Country"),
    "languages": _("Languages"),
    "cast": _("Cast"),
    "people": _("People"),
    "isbn": _("ISBN"),
    "physical_format": _("Physical Format"),
    "parent_game": _("Parent Game"),
    "parent_show": _("Parent TV Show"),
    "parent_season": _("Parent Season"),
    "related_anime": _("Related Anime"),
    "related_manga": _("Related Manga"),
    "recommendations": _("Recommendations"),
    "other_editions": _("Other Editions"),
    "remasters": _("Remasters"),
    "remakes": _("Remakes"),
    "expansions": _("Expansions"),
    "dlcs": _("DLCs"),
    "standalone_expansions": _("Standalone Expansions"),
    "expanded_games": _("Expanded Games"),
    "source": _("Source"),
    "broadcast": _("Broadcast"),
    "status_in_country_of_origin": _("Status in Country of Origin"),
    "external_links": _("External Links"),
    "providers": _("Watch Providers"),
    "tvdb_id": _("TVDB ID"),
    "last_episode_season": _("Last Episode Season"),
    "next_episode_season": _("Next Episode Season"),
    }

    return label_map.get(
        label_key,
        label_key.replace("_", " ").title(),
    )


@register.filter
def translate_media_form(label_key):
    label_map = {
        "Score": _("Score"),
        "progress": _("Progress"),
        "Status": _("Status"),
        "Start date": _("Start Date"),
        "End date": _("End Date"),
        "Notes": _("Notes"),
    }
    
    return label_map.get(
        label_key,
        label_key.replace("_", " ").title(),
    )
