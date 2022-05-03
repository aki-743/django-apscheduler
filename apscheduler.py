import os

import requests
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler


load_dotenv()

scheduler = BackgroundScheduler()


def prevent_heroku_sleep():
    """
    Herokuで30分アクセスがなかったときにサーバーがダウンするのを防ぐ

    25分毎に実行
    """

    requests.get(os.environ['ORIGIN_URL'])


scheduler.add_job(prevent_heroku_sleep, 'interval', minutes=25)
