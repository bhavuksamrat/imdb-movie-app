from django.db import models

"""
Movie Genre model
Fields:
description(charField) - Descrition of type of genre
"""
class Genre(models.Model):
    description = models.CharField(max_length=300)
    def __unicode__(self):
        return self.description

"""
Movie model
Fields:
name(charField) - Descrition of type of genre
genre(ManyToManyField) - movie genre  (servers as a foreign key to genre model)
popularity(decimalField) - movie popularity
director(charField) - Movie director
imdb_score(charField) - imdb score of a particular movie
"""
class Movie(models.Model):
    name = models.CharField(max_length = 500)
    genre = models.ManyToManyField(Genre)
    popularity = models.DecimalField(max_digits=4,decimal_places=2)
    director = models.CharField(max_length = 500)
    indb_score = models.DecimalField(max_digits=4,decimal_places=1)
    def __unicode__(self):
        return self.name
