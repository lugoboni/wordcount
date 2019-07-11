from django.urls import path

from word_count.core.views import (WordCountFormView)

app_name = "users"
urlpatterns = [
    path("~word-count/", view=WordCountFormView, name="word-count"),
]
