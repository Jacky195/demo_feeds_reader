from utils.HTTPUtils import HTTPUtils
from crawlers.models import Item
from crawlers.sites.base_site import BaseSite
from crawlers.sites.base_function import BaseFunction
from crawlers.sites.washingtonpost.settings import CHANNEL_LIST, NAME_SPACE, DATE_FORMAT, SOURCE_CODE
from utils.Constants import LIMIT_ALL
from utils.MiscUtils import MiscUtils

import logging
logger = logging.getLogger('crawlers')


class WashingtonPostSite(BaseSite):

    def __init__(self, **kwargs):
        self.limit = kwargs.get('limit')

    @classmethod
    def save_item(cls, element):
        item = Item()
        item.source_code = SOURCE_CODE.lower()
        item.author = element.find('dc:creator', NAME_SPACE).text
        item.title = element.find('title').text
        item.description = element.find('description').text
        item.original_url = element.find('link').text
        pub_date = element.find('pubDate').text
        item.date_published = MiscUtils.string_to_datetime(pub_date, DATE_FORMAT)
        item.save()

    def fetch_all(self):
        BaseFunction.fetch_all_xml(self.limit, SOURCE_CODE, CHANNEL_LIST, self.save_item)