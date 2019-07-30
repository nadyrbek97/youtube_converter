from django import forms
from .models import YoutubeFile


class YoutubeFileForm(forms.ModelForm):

    class Meta:
        model = YoutubeFile
        fields = ('link', 'email')
