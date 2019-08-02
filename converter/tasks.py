from youtube_converter.celery import app
from youtube_dl.utils import DownloadError

from .services import convert
import celery


@app.task()
def convert_task(youtube_link, email):
    return convert(youtube_link, email)



