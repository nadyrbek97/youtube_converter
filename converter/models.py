from django.db import models


class YoutubeFile(models.Model):
    link = models.URLField()
    email = models.EmailField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link
