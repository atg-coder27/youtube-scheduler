from .views import *
from django.urls import path

urlpatterns = [
    path('get_vidoes_by_query/', GetVideosByQueryView.as_view()),
]