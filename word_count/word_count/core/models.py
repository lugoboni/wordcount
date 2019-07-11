from django.db import models

class WordCount(models.Model):
    words = models.TextField()