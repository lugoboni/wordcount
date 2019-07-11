from django.db import models

class WordCount(models.Model):
    words = models.TextField(min_length=1)