from django.conf.urls import patterns, include, url

from django.contrib import admin
import imdb.views as views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'movieData',views.getStaticData,name='getStaticData'),
    url(r'^',views.index,name='index' ),
)
