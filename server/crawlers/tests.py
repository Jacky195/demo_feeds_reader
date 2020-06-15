from django.test import TestCase
from crawlers.models import Item
from utils.MiscUtils import MiscUtils

ITEM_SAMPLE = {
    "source_code": "test_source_code",
    "author": "test_author",
    "title": "test_title",
    "description": "test_description",
    "original_url": "test_original_url"
}


class ItemTestCase(TestCase):

    def setUp(self):
        item = Item.objects.create(
                                    source_code=ITEM_SAMPLE["source_code"],
                                    author=ITEM_SAMPLE["author"],
                                    title=ITEM_SAMPLE["title"],
                                    description=ITEM_SAMPLE["description"],
                                    original_url=ITEM_SAMPLE["original_url"],
                                    date_published=MiscUtils.now_date(),
                                    date_fetched=MiscUtils.now_date()
                                    )
        self.item_id = item.id

    def test_get_by_id(self):
        item = Item.get_by_id(self.item_id)
        self.assertEqual(item.get_source_code(), ITEM_SAMPLE['source_code'])
        self.assertEqual(item.get_author(), ITEM_SAMPLE['author'])
        self.assertEqual(item.get_title(), ITEM_SAMPLE['title'])
        self.assertEqual(item.get_description(), ITEM_SAMPLE['description'])
        self.assertEqual(item.get_original_url(), ITEM_SAMPLE['original_url'])
