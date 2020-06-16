# I don't implement this management command
# Ideally: Fetch ALL, but only get the feeds which satisfy one of the following conditions:
#   + Not fetched yet, not saved in Feed Store: Have "Publish Date" or "Create Date" is after than "Last run timestamp".
#       We need to save the "Last run timestamp" of all times we fetch certain sources.
#   + If fetched and saved already in Feed Store: Have "Last Modified Date" is after than "Last Modified Date"
#       of Saved Feed.

from crawlers.management.base_command import CrawlerCommand


class Command(CrawlerCommand):
    help = 'Only fetch the updated feeds in specific sites'

    def handle(self, *args, **options):
        pass
