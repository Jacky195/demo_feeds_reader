from django.db import models


class Item(models.Model):
    source_code = models.CharField(max_length=20)  # wstp (washingtonpost), nyt (nytimes), npr etc.
    # item fields
    title = models.TextField(default='')
    description = models.TextField(default='')
    original_url = models.TextField(default='')
    date_published = models.DateTimeField(null=True)
    date_modified = models.DateTimeField(null=True)
    # custom fields
    date_fetched = models.DateTimeField(null=True)
