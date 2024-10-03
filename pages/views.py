from django.shortcuts import render
from .models import Page

def page(request, url):
    cnxt: dict = {}
    page = Page.objects.get(url=request.path)
    cnxt["page"] = page
    cnxt["subpages"] = Page.objects.filter(parent=page).order_by('pk')
    return render(request, 'pages/index.html', cnxt)
