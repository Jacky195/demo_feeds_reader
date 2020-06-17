from django.db import models
from utils.MiscUtils import MiscUtils
from utils.Constants import TRUNCATED_TEXT_LENGTH_SHORT, TRUNCATED_TEXT_LENGTH_LONG
import logging
logger = logging.getLogger('crawlers')

class Feed(models.Model):
    source_code = models.CharField(max_length=100)
    # item fields
    author = models.TextField(default='')
    title = models.TextField(default='')
    description = models.TextField(default='')
    original_url = models.TextField(default='')
    date_published = models.DateTimeField(null=True)
    # custom fields
    date_fetched = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.date_fetched = MiscUtils.now_date()
        super(Feed, self).save(*args, **kwargs)

    def get_source_code(self):
        return self.source_code

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def get_title_truncated(self, size=TRUNCATED_TEXT_LENGTH_SHORT):
        txt = self.title[:size]
        return txt if len(self.title) <= size else "{}...".format(txt)

    def get_description(self):
        return self.description

    def get_description_truncated(self, size=TRUNCATED_TEXT_LENGTH_LONG):
        txt = MiscUtils.strip_html_tags(self.description)[:size]
        return txt if len(self.description) <= size else "{}...".format(txt)

    def get_original_url(self):
        return self.original_url

    def get_date_published(self):
        return MiscUtils.datetime_to_string(self.date_published)

    def to_json(self):
        return {
            'source_code': self.get_source_code(),
            'author': self.get_author(),
            'title': self.get_title(),
            'title_truncated': self.get_title_truncated(),
            'description': self.get_description(),
            'description_truncated': self.get_description_truncated(),
            'original_url': self.get_original_url(),
            'date_published': self.get_date_published()
        }

    @staticmethod
    def get_by_id(id):
        try:
            return Feed.objects.get(id=id)
        except e:
            return None

    @staticmethod
    def get_all(page, limit, keyword):
        try:
            feeds = Feed.objects.filter(source_code__icontains=keyword)
            total_count = feeds.count()
            feeds = feeds[(page-1)*limit:page*limit]
            idx = (page-1)*limit
            result = []
            for feed in feeds:
                idx += 1
                feed_obj = feed.to_json()
                feed_obj['idx'] = idx
                result.append(feed_obj)
            return {
                'feeds': result,
                'totalPage': int(total_count / limit) + 1
            }
        except Exception as e:
            logger.error(e)
            return []

