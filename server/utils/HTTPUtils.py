from django.http import HttpResponse
import requests
import json
from xml.etree import ElementTree
import logging
logger = logging.getLogger('crawlers')


class HTTPUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_xml_response(url, params=None):
        try:
            resp = requests.get(url, params=params)
            return ElementTree.fromstring(resp.text)
        except Exception as e:
            logger.error(e)
            return None

    @staticmethod
    def format_data_for_ajax(data):
        if isinstance(data, dict) and ('status' not in data):
            data['status'] = 'success'
        return HttpResponse(json.dumps(data), content_type='application/json')
