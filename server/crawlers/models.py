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

    def set_source_code(self, source):
        self.source_code = source

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_title(self):
        return self.title

    def get_title_truncated(self, size=TRUNCATED_TEXT_LENGTH_SHORT):
        txt = self.title[:size]
        return txt if len(self.title) <= size else "{}...".format(txt)

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def get_description_truncated(self, size=TRUNCATED_TEXT_LENGTH_LONG):
        txt = MiscUtils.strip_html_tags(self.description)[:size]
        return txt if len(self.description) <= size else "{}...".format(txt)

    def set_description(self, description):
        self.description = description

    def get_original_url(self):
        return self.original_url

    def set_original_url(self, url):
        self.original_url = url

    def get_date_published(self):
        return MiscUtils.datetime_to_string(self.date_published)

    def set_date_published(self, date_obj):
        self.date_published = date_obj

    def get_date_fetched(self):
        return MiscUtils.datetime_to_string(self.date_fetched)

    def to_json(self):
        return {
            'id': self.id,
            'source_code': self.get_source_code(),
            'author': self.get_author(),
            'title': self.get_title(),
            'title_truncated': self.get_title_truncated(),
            'description': self.get_description(),
            'description_truncated': self.get_description_truncated(),
            'original_url': self.get_original_url(),
            'date_published': self.get_date_published(),
            'date_fetched': self.get_date_fetched()
        }

    @staticmethod
    def get_by_id(id):
        try:
            return Feed.objects.get(id=id)
        except e:
            logger.error(e)
            return None

    @staticmethod
    def delete_by_id(id):
        try:
            Feed.objects.get(id=id).delete()
            return 'success'
        except e:
            logger.error(e)
            return 'Cannot delete feed id: {}'.format(id)


    @staticmethod
    def get_all(page, limit, keyword):
        try:
            feeds = Feed.objects.filter(source_code__icontains=keyword).order_by('-date_fetched')
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
                'totalPage': int((total_count-1) / limit) + 1
            }
        except Exception as e:
            logger.error(e)
            return []

    @staticmethod
    def get_all_sources():
        try:
            sources = Feed.objects.all().values_list('source_code', flat=True).distinct()
            return sources
        except Exception as e:
            logger.error(e)
            return []

    @staticmethod
    def create_or_update(source, title, description, url=None, feed_id=None):
        try:
            if not feed_id:
                feed = Feed()
                feed.set_date_published(MiscUtils.now_date())
            else:
                feed = Feed.get_by_id(feed_id)
            feed.set_source_code(source)
            feed.set_title(title)
            feed.set_description(description)
            feed.set_original_url(url)
            feed.save()
            return "success"
        except Exception as e:
            logger.error(e)
            return "Cannot create feed"

