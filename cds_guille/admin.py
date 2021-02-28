from django.contrib import admin
from .models import Album, Band

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'artist', 'original')

class BandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')