from rest_framework import serializers
from .models import Album, Band

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'year', 'artist', 'original')

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ('id', 'name')