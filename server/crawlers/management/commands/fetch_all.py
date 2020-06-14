from crawlers.management.base_command import CrawlerCommand
from django.conf import settings
import importlib
import logging

logger = logging.getLogger('crawlers')
NEW_LINE = '\n----------------\n'
LIMIT_ALL = 'ALL'


class Command(CrawlerCommand):
    help = 'Fetch all the items in specific sites'

    def handle(self, *args, **options):
        sites = options.get('sites')
        limit = options.get('limit') if options.get('limit') else LIMIT_ALL
        try:
            if sites == 'all':
                site_list = map(
                    lambda c: importlib.import_module('%s' % c),
                    settings.FEED_SITES
                )
            else:
                site_list = [importlib.import_module('crawlers.sites.%s' % site) for site in sites.split(',')]
            for s in site_list:
                site = s.get_site(limit=limit)
                site.fetch_all()
        except ModuleNotFoundError as e:
            logger.error(e)


