from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=50)
    url = models.CharField(max_length=500, default="/", unique=True)

    class Meta:
        ordering = ["pk",]
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Verse(models.Model):
    """Стихи."""
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    verse_number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.page.name}:{self.verse_number} {self.page.title} '

    class Meta:
        ordering = ["pk",]