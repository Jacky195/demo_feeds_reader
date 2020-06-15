from django.db import models
from utils.MiscUtils import MiscUtils


class Item(models.Model):
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
        super(Item, self).save(*args, **kwargs)

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


    @staticmethod
    def get_by_id(id):
        try:
            return Item.objects.get(id=id)
        except e:
            return None

