from django.core.management.base import BaseCommand, CommandError
from pages.models import Page, Verse
import json
import pathlib
from pprint import pprint

class Command(BaseCommand):
    help = "Import bible"

    def add_arguments(self, parser):
        parser.add_argument("file", nargs="+", type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        self.stdout.write(self.style.SUCCESS(f"File: {options['file'][0]}"))
        bible_path = pathlib.Path(options['file'][0])
        sql = "DELETE FROM "
        if not bible_path.exists():
            raise CommandError("No file with bible.")
        fh = open(bible_path, "rb")
        bible_data = json.load(fh)
        # print(len(bible_data))
        # pprint(bible_data[1], depth=7)
        parent_id = 1
        parent_page = Page.objects.get(id=parent_id)
        cnt = 1
        Page.objects.filter(pk__gt=1).delete()
        Verse.objects.all().delete()
        for item in bible_data:
            print(cnt)
            print(item["name"])
            print(item["abbrev"])
            print(len(item["chapters"]))
            page = Page(
                name=item["name"],
                parent=parent_page,
                slug=item["abbrev"],
                url=parent_page.url + item["abbrev"] + "/",
            )
            page.save()

            chapter_cnt = 1
            for chapter in item["chapters"]:
                print(f"chapter: {chapter_cnt}")
                page2 = Page(
                    name=str(chapter_cnt),
                    slug=str(chapter_cnt),
                    parent=page,
                    url=page.url + str(chapter_cnt) + "/",
                )
                page2.save()
                verse_cnt = 1
                for verse in chapter:
                    print(f"\t{item["abbrev"]}:{chapter_cnt}:{verse_cnt} {verse[1:20]}")
                    v = Verse(
                        page=page2,
                        verse_number=verse_cnt,
                        text=verse,
                    )
                    v.save()
                    verse_cnt = verse_cnt + 1
                chapter_cnt = chapter_cnt + 1
            cnt = cnt + 1
            print("---------------------------------------")
