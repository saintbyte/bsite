from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Page(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class Verse(models.Model):
    """Стихи."""
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    verse_number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.page.title} {self.verse_number}'