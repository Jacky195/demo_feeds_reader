from django.test import TestCase
from crawlers.models import Feed
from utils.MiscUtils import MiscUtils

FEED_SAMPLE = {
    "source_code": "test_source_code",
    "author": "test_author",
    "title": "test_title",
    "description": "test_description",
    "original_url": "test_original_url"
}


class FeedTestCase(TestCase):

    def setUp(self):
        feed = Feed.objects.create(
                                    source_code=FEED_SAMPLE["source_code"],
                                    author=FEED_SAMPLE["author"],
                                    title=FEED_SAMPLE["title"],
                                    description=FEED_SAMPLE["description"],
                                    original_url=FEED_SAMPLE["original_url"],
                                    date_published=MiscUtils.now_date(),
                                    date_fetched=MiscUtils.now_date()
                                    )
        self.feed_id = feed.id

    def test_get_by_id(self):
        feed = Feed.get_by_id(self.feed_id)
        self.assertEqual(feed.get_source_code(), FEED_SAMPLE['source_code'])
        self.assertEqual(feed.get_author(), FEED_SAMPLE['author'])
        self.assertEqual(feed.get_title(), FEED_SAMPLE['title'])
        self.assertEqual(feed.get_description(), FEED_SAMPLE['description'])
        self.assertEqual(feed.get_original_url(), FEED_SAMPLE['original_url'])
