from django.core.management.base import BaseCommand, CommandError
from pages.models import HomePage, Verse
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
        parent_id = 73
        parent_page = HomePage.objects.get(id=parent_id)
        cnt = 1

        for item in bible_data:
            print(cnt)
            print(item["name"])
            print(item["abbrev"])
            print(len(item["chapters"]))
            page = HomePage(
                title=item["name"],
                slug=item["abbrev"],
                seo_title=item["name"],
                live=True,
                url_path=parent_page.url_path + item["abbrev"] + "/",
                path=parent_page.path + str(cnt).zfill(4),
                depth=4,
            )
            page.save()

            chapter_cnt = 1
            for chapter in item["chapters"]:
                print(f"chapter: {chapter_cnt}")
                page2 = HomePage(
                    title=str(chapter_cnt),
                    slug=str(chapter_cnt),
                    seo_title=str(chapter_cnt),
                    live=True,
                    url_path=page.url_path + str(chapter_cnt) + "/",
                    path=page.path + str(chapter_cnt).zfill(4),
                    depth=5,
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
