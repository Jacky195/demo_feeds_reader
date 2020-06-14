from crawlers.management.base_command import CrawlerCommand
import logging
logger = logging.getLogger('crawlers')


class Command(CrawlerCommand):
    help = 'Fetch all the items in specific sites'

    def handle(self, *args, **options):
        sites = options.get('sites')
        limit = options.get('limit')
        message = "sites: {} - limit: {}".format(sites, limit)
        logger.debug(message)
