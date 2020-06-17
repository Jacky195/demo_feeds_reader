from django.core.cache import cache
from django.db import models
from django.conf import settings
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
            cache_key = MemCache.gen_key([id])
            cache_obj = MemCache.get_cache(cache_key)
            if cache_obj:
                return cache_obj
            # no cache hit
            feed = Feed.objects.get(id=id)
            # save to cache
            MemCache.set_cache(cache_key, feed)
            return feed
        except e:
            logger.error(e)
            return None

    @staticmethod
    def delete_by_id(id):
        try:
            Feed.objects.get(id=id).delete()
            # remove cache
            cache_key = MemCache.gen_key([id])
            MemCache.delete_cache(cache_key)
            # clear cache for datatable
            MemCache.delete_cache_datatable()
            return 'success'
        except e:
            logger.error(e)
            return 'Cannot delete feed id: {}'.format(id)

    @staticmethod
    def get_all(page, limit, keyword):
        try:
            cache_key = MemCache.gen_key(['datatable', keyword, limit, page])
            cache_obj = MemCache.get_cache(cache_key)
            if cache_obj:
                # we need to update the "date_fetched" fields, and "Feed.get_by_id" will hit cache
                feeds = cache_obj['feeds']
                result = []
                for feed in feeds:
                    feed_tmp = Feed.get_by_id(feed['id']).to_json()
                    feed['date_fetched'] = feed_tmp['date_fetched']
                    result.append(feed)
                cache_obj['feeds'] = result
                return cache_obj

            # no cache hit
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
            cache_obj = {
                'feeds': result,
                'totalPage': int((total_count-1) / limit) + 1,
                'totalFeed': total_count
            }
            # save to cache
            MemCache.set_cache(cache_key, cache_obj)
            return cache_obj
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
            # clear cache for datatable
            MemCache.delete_cache_datatable()
            # save to cache
            cache_key = MemCache.gen_key([feed.id])
            MemCache.set_cache(cache_key, feed)
            return "success"
        except Exception as e:
            logger.error(e)
            return "Cannot create feed"


# using Redis
class MemCache:

    def __init__(self):
        pass

    @staticmethod
    def gen_key(lst):
        new_lst = [str(obj) for obj in lst]
        return '_'.join(new_lst)

    @staticmethod
    def get_cache(key, default_value=None):
        value = cache.get(key)
        return value if value else default_value

    @staticmethod
    def set_cache(key, value, timeout=settings.CACHE_TIMEOUT_UNTIL_DELETED):
        cache.set(key, value, timeout)

    @staticmethod
    def delete_cache(key):
        cache.delete(key)

    @staticmethod
    def delete_cache_pattern(pattern):
        cache.delete_pattern(pattern)

    @staticmethod
    def delete_cache_datatable():
        MemCache.delete_cache_pattern("datatable_*")