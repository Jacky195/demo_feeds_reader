from datetime import datetime
from django.utils.html import strip_tags


class MiscUtils:
    def __init__(self):
        pass

    @staticmethod
    def now_date():
        return datetime.utcnow()

    @staticmethod
    def string_to_datetime(txt, date_format):
        return datetime.strptime(txt, date_format)

    @staticmethod
    def datetime_to_string(date_object, date_format="%Y-%m-%d %H:%M:%S"):
        return datetime.strftime(date_object, date_format)

    @staticmethod
    def strip_html_tags(txt):
        return strip_tags(txt)

