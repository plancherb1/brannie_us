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
from version1 import views as weddingViews

# main url patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', weddingViews.index, name='index'), # update when out of wedding mode

    # wedding pages
    url(r'^wedding$', weddingViews.index, name='wedding'),
    url(r'^wedding/hotels', weddingViews.hotels, name='weddingHotels'),
    url(r'^wedding/saturday', weddingViews.saturday, name='weddingSaturday'),
    url(r'^wedding/restaurants', weddingViews.restaurants, name='weddingRestaurants'),
    url(r'^wedding/activities', weddingViews.activities, name='weddingActivities'),
    url(r'^wedding/travel', weddingViews.travel, name='weddingTravel'),
    #url(r'getImage/(?P<id>[0-9]+)/$', weddingViews.getImage, name='getImage'),
]

# handle the 404 error
handler404 = weddingViews.error404 # update when out of wedding mode

# handle static files
urlpatterns += staticfiles_urlpatterns()