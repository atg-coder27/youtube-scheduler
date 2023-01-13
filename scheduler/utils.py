
from datetime import datetime,timedelta,timezone
import requests

def get_data(api_key, part, order,search_query, maxResults,publishedAfter):
    url = f"https://youtube.googleapis.com/youtube/v3/search?" \
          f"part={part}&" \
          f"maxResults={maxResults}&" \
          f"order={order}&" \
          f"publishedAfter={publishedAfter}&" \
          f"q={search_query}&" \
          f"key={api_key}"
    return requests.get(url=url)


def get_previous_time():
    utc_past_hour = datetime.utcnow() + timedelta(minutes=-10)
    my_time = str(utc_past_hour.replace(tzinfo=timezone.utc)).split(' ')
    return f"{my_time[0]}T{my_time[1][:-6]}Z"