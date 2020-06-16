from django.db import models
from utils.MiscUtils import MiscUtils
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

    def get_description(self):
        return self.description

    def get_original_url(self):
        return self.original_url

    def get_date_published(self):
        return MiscUtils.datetime_to_string(self.date_published)

    def to_json(self):
        return {
            'source_code': self.get_source_code(),
            'author': self.get_author(),
            'title': self.get_title(),
            'description': self.get_description(),
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
            feeds = Feed.objects.filter(source_code__icontains=keyword)[(page-1)*limit:page*limit]
            feeds = [feed.to_json() for feed in feeds]
            logger.debug(feeds)
            return feeds
        except Exception as e:
            logger.error(e)
            return []

