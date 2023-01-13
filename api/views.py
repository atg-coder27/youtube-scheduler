import json
from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework import status
from .models import YoutubeVideo
from .serializer import YoutubeSerializer
from config.cache import RedisHash
from django.db.models import Q
from django.core.paginator import Paginator
import os

# Create your views here.

class GetVideosByQueryView(generics.GenericAPIView,mixins.ListModelMixin):
    """ API View to fetch youtube data from the database """
    def get(self,request,*args,**kwargs):
        query = request.GET.get("query")
        tag_title = request.GET.get("title")
        page_no = request.GET.get("page_no")
        try:
            value = RedisHash().get_value("TAGS",tag_title)

            if value == None:
                value = 0
            else:
                value = json.loads(value)
            value += 1
            RedisHash().add_to_hash("TAGS",tag_title,json.dumps(value))
            vidoes = YoutubeVideo.objects.filter(Q(title__icontains = query) | Q(description__icontains=query)).order_by("-published_time")
            paginator = Paginator(vidoes,5)
            videos_per_page = paginator.get_page(page_no)
            response = YoutubeSerializer(videos_per_page.object_list,many = True)
            return Response({"data":response.data,"error":False},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": True, "message": str(e)})
