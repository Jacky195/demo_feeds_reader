from django.core.management.base import BaseCommand


class CrawlerCommand(BaseCommand):

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--limit',
            '-l',
            default=0,
            type=int,
            help='Number of items the site will be iterated through. No input means fetched all the items'
        )

        parser.add_argument(
            '--sites',
            '-s',
            default='all',
            help='Which sites will be fetched. Multiple sites will be separated by comma, and "all" for all sites'
        )

