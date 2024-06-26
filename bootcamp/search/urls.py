from django.urls import re_path

from bootcamp.search import views

app_name = "search"
urlpatterns = [
    re_path(r"^$", views.SearchListView.as_view(), name="results"),
    re_path(r"^suggestions/$", views.get_suggestions, name="suggestions"),
]
