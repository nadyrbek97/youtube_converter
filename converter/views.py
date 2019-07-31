from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import YoutubeFileForm
from .services import Converter
from .models import YoutubeFile

from youtube_dl.utils import DownloadError


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            try:
                # pass video_link to converter
                video_link = Converter.convert(link, email)
                # save it
                YoutubeFile.objects.create(link=video_link, email=email)
                # success message
                messages.success(request, 'We sent download link to your email, please check it.')
                return render(request, 'converter/home.html', {'form': form})
            except DownloadError:
                # error message
                messages.error(request, 'Unsupported URL, please put valid YOUTUBE url')
                return render(request, 'converter/home.html', {'form': form})

    form = YoutubeFileForm(request.GET)
    return render(request, 'converter/home.html', {'form': form})
