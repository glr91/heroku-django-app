"""djangoherokuapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers                     
from django.views.generic import TemplateView
from cds_guille import views 

router = routers.DefaultRouter()   
router.register(r'albums', views.AlbumsView, basename='albums')
router.register(r'albums-band', views.AlbumsBandView, basename='albums-band')
router.register(r'albums-band-tree', views.AlbumsBandNodesTreeView, basename='albums-band-tree')
router.register(r'bands', views.BandsView, basename='bands')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('', views.FrontendAppView.as_view()),
]
