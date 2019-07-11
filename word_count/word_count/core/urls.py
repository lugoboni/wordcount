from django.urls import path

from word_count.core.views import (WordCountFormView)

app_name = "core"
urlpatterns = [
    path("word-count/", view=WordCountFormView.as_view(), name="word-count"),
]
