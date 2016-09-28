from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    playlist_embed_tag = models.CharField(max_length=250, default="")
    playlist_url = models.URLField()
