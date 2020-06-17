from datetime import datetime, timedelta
from django.utils.html import strip_tags
import arrow


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
        if date_object > MiscUtils.now_date() - timedelta(days=1):  # within a day
            return arrow.get(date_object).humanize()
        else:
            return datetime.strftime(date_object, date_format)

    @staticmethod
    def strip_html_tags(txt):
        return strip_tags(txt)

