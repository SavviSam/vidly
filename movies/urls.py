from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path(route="", view=views.index, name="index"),
    path(route="<int:movie_id>", view=views.detail, name="detail"),
]
