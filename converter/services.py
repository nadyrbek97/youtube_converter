from django.core.mail import send_mail

from youtube_converter import settings

import youtube_dl
from youtube_dl.utils import DownloadError


def convert(youtube_link, email):
    """
        Task to download video and convert it to mp3 format
        """
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            info = ydl.extract_info(youtube_link)
            # replacing spaces with %20
            file_title = info['title'].replace(" ", "%20")
            video_link = 'http://127.0.0.1:8000/media/music/' + file_title + '.mp3'
            # send email
            mail_send(email, video_link)
            return video_link
        except DownloadError:
            pass


def mail_send(email, link):
    send_mail(
        'Link for downloading mp3 format',
        link,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )