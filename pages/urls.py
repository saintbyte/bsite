from .views import page
from django.urls import path, re_path
urlpatterns = [
  re_path(r"^(?P<path>.*)$", page, name="page"),
]