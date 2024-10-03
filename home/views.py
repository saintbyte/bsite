from django.shortcuts import render
from pages.models import Page
from .constants import HOME_PATH


def home(request):
    cnxt: dict = {}
    home_page = Page.objects.get(url=HOME_PATH)
    cnxt["home_page"] = home_page
    cnxt["subpages"] = Page.objects.filter(parent=home_page).order_by('pk')
    return render(request, "home/index.html", cnxt)
