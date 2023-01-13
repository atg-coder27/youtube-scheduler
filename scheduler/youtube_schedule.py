import json
import requests
import os
from datetime import datetime, timedelta, timezone
from api.models import YoutubeVideo
from django.conf import settings
from config.cache import RedisHash
from .utils import *
from . import constants

def get_maximum_selected_value():
    try:
        query_tags = RedisHash().get_all_key_values("TAGS")
        search_query = None
        if query_tags:
            query_order = []
            for i in query_tags:
                value = query_tags[i].decode("utf-8")
                key = i.decode("utf-8")
                query_order.append([value,key])
            
            query_order.sort(reverse = True)
            search_query = query_order[0][1]
        print(search_query)
        return search_query
    except:
        return None

def schedule():
    search_query = get_maximum_selected_value()
    if search_query == None:
        search_query = constants.SEARCH_QUERY
    
    api_keys = constants.API_KEYS
    part = constants.PART
    maxResults = constants.MAX_RESULTS
    order = constants.ORDER
    publishedAfter = get_previous_time()
    try:
        for developer_key in api_keys:
            response = get_data(api_key=developer_key,part=part,maxResults=maxResults,search_query=search_query,order=order,publishedAfter=publishedAfter)
            if response.status_code == 400 or response.status_code == 403:
                print("Key Expired or credits used")
                continue

            if response.status_code == 200:
                print(response.status_code)
                items = response.json()["items"]
                can_break = False
                for item in items:
                    try:
                        YoutubeVideo.objects.update_or_create(
                            title=item["snippet"]["title"],
                            description=item["snippet"]["description"],
                            published_time=item["snippet"]["publishedAt"],
                            thumbnail_url=item["snippet"]["thumbnails"]["default"]["url"],
                            video_id=item["id"]["videoId"],
                            channel_title=item["snippet"]["channelTitle"],
                            channel_id=item["snippet"]["channelId"],
                        )
                        can_break = True

                    except Exception as e:
                        '''
                        Only unique entries will be saved.
                        Uniqueness is identified using video_id from youtube.com
                        '''
                        print(e)
                if can_break:
                    break
        print(f"Database updated with new entries of {search_query}")
    except Exception as e:
        print(e)

   
        




    

    