from django.shortcuts import render
from rest_framework import viewsets    
from .serializers import AlbumSerializer, BandSerializer     
from .models import Album, Band    
from django.views import View
from django.http import HttpResponse
from django.conf import settings
import os     
import logging      

class AlbumsView(viewsets.ModelViewSet):       
    serializer_class = AlbumSerializer          
    queryset = Album.objects.all()          

class BandsView(viewsets.ModelViewSet):       
    serializer_class = BandSerializer          
    queryset = Band.objects.all()       

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    build`).
    """
    index_file_path = os.path.join(settings.BASE_DIR, 'build', 'index.html')

    def get(self, request):
        try:
            with open(self.index_file_path) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead after
                running `yarn start` on the frontend/ directory
                """,
                status=501,
            )