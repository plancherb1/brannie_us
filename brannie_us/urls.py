"""brannie_us URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from . import settings
#pick which app/version to use here
from version1 import views

# main url patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wedding$', views.wedding, name='wedding'),
    url(r'^wedding/directions', views.weddingDirections, name='weddingDirections'),
    url(r'^wedding/hotels', views.weddingHotels, name='weddingHotels'),
    #url(r'getImage/(?P<id>[0-9]+)/$', views.getImage, name='getImage'),
    url(r'^$', views.index, name='index'),
]

# handle the 404 error
handler404 = views.error404

# handle static files
urlpatterns += staticfiles_urlpatterns()