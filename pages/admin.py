from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from pages.models import Page


class PageMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Page, PageMPTTModelAdmin)
