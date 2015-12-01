from django.contrib import admin
from imdb.models import Genre,\
                        Movie
"""Registering the Models, so that admin interface can directly access and input data for it"""
admin.site.register(Genre)
admin.site.register(Movie)
