from django.shortcuts import render
from .forms import YoutubeFileForm


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            return render(request, 'converter/home.html', {'form': form})
    form = YoutubeFileForm(request.GET)
    return render(request, 'converter/home.html', {'form': form})
