from django.shortcuts import render
from rest_framework import viewsets    
from .serializers import AlbumSerializer, BandSerializer     
from .models import Album, Band    
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os                

class AlbumsView(viewsets.ModelViewSet):       
    serializer_class = AlbumSerializer          
    queryset = Album.objects.all()          

class BandsView(viewsets.ModelViewSet):       
    serializer_class = BandSerializer          
    queryset = Band.objects.all()       

class Assets(View):
    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()