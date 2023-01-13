from rest_framework import serializers
from .models import YoutubeVideo


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'