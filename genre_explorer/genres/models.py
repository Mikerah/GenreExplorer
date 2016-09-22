from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    playlist_url = models. CharField(max_length=250)
