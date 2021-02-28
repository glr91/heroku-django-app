from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import AlbumSerializer, BandSerializer     
from .models import Album, Band                    

class AlbumsView(viewsets.ModelViewSet):       
    serializer_class = AlbumSerializer          
    queryset = Album.objects.all()          

class BandsView(viewsets.ModelViewSet):       
    serializer_class = BandSerializer          
    queryset = Band.objects.all()       
