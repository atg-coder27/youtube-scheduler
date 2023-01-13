from django.contrib import admin
from .models import YoutubeVideo

# Register your models here.
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id','title','createdAt')

@admin.register(YoutubeVideo)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'description', 'published_time', 'thumbnail_url','channel_title','channel_id',)

# @admin.register(TaggedVideo)
# class TaggedVideoAdmin(admin.ModelAdmin):
#     list_display = ('tag','video')