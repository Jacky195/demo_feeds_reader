import requests
from xml.etree import ElementTree
import logging
logger = logging.getLogger('crawlers')


class HTTPUtils:
    def __init__(self):
        pass

    @classmethod
    def get_xml_response(cls, url, params=None):
        try:
            resp = requests.get(url, params=params)
            return ElementTree.fromstring(resp.text)
        except Exception as e:
            logger.error(e)
            return None
