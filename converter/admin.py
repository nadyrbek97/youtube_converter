from django.contrib import admin
from .models import YoutubeFile


@admin.register(YoutubeFile)
class YoutubeFileAdmin(admin.ModelAdmin):
    list_display = ('link', 'email')

