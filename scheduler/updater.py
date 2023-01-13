from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import youtube_schedule


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(youtube_schedule.schedule,'interval',seconds = 20)
    scheduler.start()