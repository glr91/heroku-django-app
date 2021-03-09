from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .serializers import AlbumSerializer, BandSerializer, TreeParentNodeSerializer, TreeChildNodeSerializer   
from .models import Album, Band    
from django.views import View
from django.http import HttpResponse
from django.conf import settings
import os     
import logging      

# FIXME: only allow GET requests in all the views, do not allow POSTS/PUTS/DELETES and so on


class AlbumsView(viewsets.ModelViewSet):       
    serializer_class = AlbumSerializer          
    queryset = Album.objects.all()
    http_method_names = ['get']
        

class BandsView(viewsets.ModelViewSet):       
    serializer_class = BandSerializer          
    queryset = Band.objects.all()       
    http_method_names = ['get']

class AlbumsBandView(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer    
    http_method_names = ['get']
    def get_queryset(self):
        artistId = self.request.query_params.get('artistId', None)
        if artistId is not None:
            queryset = Album.objects.filter(artist=artistId)

        else:
            queryset = Album.objects.all()  

        return queryset  

class AlbumsBandNodesTreeView(viewsets.ModelViewSet):
    serializer_class = TreeParentNodeSerializer    
    
    def get_queryset(self):
        result = []
        bands = Band.objects.order_by('name')  
        for band in bands:
            parentNode = TreeParentNodeSerializer()
            parentNode.parentId = None
            parentNode.label = band.name
            parentNode.id = band.id
            albums = Album.objects.filter(artist=band.id).order_by('title')
            childNodes = []
            for album in albums:
                childNode = TreeChildNodeSerializer()
                childNode.parentId = band.id
                childNode.label = album.title
                childNode.id = album.id
                childNodes.append(childNode)

            parentNode.items = childNodes
            result.append(parentNode)

        return result  

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