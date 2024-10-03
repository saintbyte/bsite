from django.core.management.base import BaseCommand, CommandError
from home.models import Page, Verse
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
        if not bible_path.exists():
            raise CommandError("No file with bible.")
        fh = open(bible_path, "rb")
        bible_data = json.load(fh)
        cnt = 1
        for item in bible_data:
            print(cnt)
            print(item["name"])
            print(item["abbrev"])
            print(len(item["chapters"]))
            chapter_cnt = 1
            for chapter in item["chapters"]:
                print(chapter_cnt)
                print(chapter)
                verse_cnt = 1
                for verse in chapter:
                    print(f"\t{item["abbrev"]}:{chapter_cnt}:{verse_cnt} {verse[1:20]}")
                    verse_cnt = verse_cnt + 1
                chapter_cnt = chapter_cnt + 1
            cnt = cnt + 1
            print("---------------------------------------")