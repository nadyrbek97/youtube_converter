from django.shortcuts import render
from django.contrib import messages

from .forms import YoutubeFileForm
from .tasks import convert_task


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            # we call the delay() method of the task to execute it async-ly
            convert_task.delay(link, email)
            messages.success(request, 'We sent download link to your email, please check it.')
            return render(request, 'converter/home.html', {'form': form})

    form = YoutubeFileForm(request.GET)
    return render(request, 'converter/home.html', {'form': form})
