from crawlers.sites.base_site import BaseSite
import logging

logger = logging.getLogger('crawlers')


class FeedForAll(BaseSite):

    def __init__(self, **kwargs):
        self.limit = kwargs.get('limit')

    def __str__(self):
        return 'FeedForAll'

    def fetch_all(self):
        logger.debug("[{}] Processing'".format(self.__str__()))
