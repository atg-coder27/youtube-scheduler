from rest_framework import serializers
from .models import YoutubeVideo


class YoutubeSerializer(serializers.ModelSerializer):
    """ Serializer to serialize QuerySet object into JSON based """
    class Meta:
        model = YoutubeVideo
        fields = '__all__'