import youtube_dl


def converter(video_link):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}

    with youtube_dl.YoutubeDL(options) as ydl:
        info = ydl.extract_info(video_link)
        # replacing spaces with %20
        file_title = info['title'].replace(" ", "%20")
        link = 'http://127.0.0.1:8000/media/music/' + file_title + '.mp3'
        return link
