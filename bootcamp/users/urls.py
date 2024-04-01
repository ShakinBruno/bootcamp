from django.urls import re_path

from . import views

app_name = "users"
urlpatterns = [
    re_path(regex=r"^$", view=views.UserListView.as_view(), name="list"),
    re_path(regex=r"^~redirect/$", view=views.UserRedirectView.as_view(), name="redirect"),
    re_path(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    re_path(
        regex=r"^(?P<username>[\w.@+-]+)/$",
        view=views.UserDetailView.as_view(),
        name="detail",
    ),
]
