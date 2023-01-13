

from django.db import models


class YoutubeVideo(models.Model):
    video_id = models.CharField(max_length=100, primary_key=True, db_index= True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    published_time = models.DateTimeField()
    thumbnail_url = models.URLField()
    channel_title = models.CharField(max_length=150)
    channel_id = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

    @property
    def video_url(self):
        return "https://www.youtube.com/watch?v={}".format(self.video_id)
