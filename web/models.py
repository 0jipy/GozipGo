# Create your models here.
from django.db import models

# Create your models here.
class Netflix(models.Model):
    title = models.CharField(max_length=4000, blank=True, null=True)
    opening_date = models.CharField(max_length=1000, blank=True, null=True)
    just_rating = models.CharField(max_length=1000, blank=True, null=True)
    imdb_rating = models.CharField(max_length=1000, blank=True, null=True)
    runtime = models.CharField(max_length=500, blank=True, null=True)
    synopsis = models.CharField(max_length=4000, blank=True, null=True)
    director = models.CharField(max_length=1000, blank=True, null=True)
    actors = models.CharField(max_length=4000, blank=True, null=True)
    genre = models.CharField(max_length=4000, blank=True, null=True)
    poster_link = models.CharField(max_length=1000, blank=True, null=True)
    netflix = models.IntegerField(blank=True, null=True)
    disneyplus = models.IntegerField(blank=True, null=True)
    wavve = models.IntegerField(blank=True, null=True)
    watcha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netflix'

class Disney(models.Model):
    title = models.CharField(max_length=4000, blank=True, null=True)
    opening_date = models.CharField(max_length=1000, blank=True, null=True)
    just_rating = models.CharField(max_length=1000, blank=True, null=True)
    imdb_rating = models.CharField(max_length=1000, blank=True, null=True)
    runtime = models.CharField(max_length=500, blank=True, null=True)
    synopsis = models.CharField(max_length=4000, blank=True, null=True)
    director = models.CharField(max_length=1000, blank=True, null=True)
    actors = models.CharField(max_length=4000, blank=True, null=True)
    genre = models.CharField(max_length=4000, blank=True, null=True)
    poster_link = models.CharField(max_length=1000, blank=True, null=True)
    netflix = models.IntegerField(blank=True, null=True)
    disneyplus = models.IntegerField(blank=True, null=True)
    wavve = models.IntegerField(blank=True, null=True)
    watcha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disney'


class Watcha(models.Model):
    title = models.CharField(max_length=4000, blank=True, null=True)
    opening_date = models.CharField(max_length=1000, blank=True, null=True)
    just_rating = models.CharField(max_length=1000, blank=True, null=True)
    imdb_rating = models.CharField(max_length=1000, blank=True, null=True)
    runtime = models.CharField(max_length=500, blank=True, null=True)
    synopsis = models.CharField(max_length=4000, blank=True, null=True)
    director = models.CharField(max_length=1000, blank=True, null=True)
    actors = models.CharField(max_length=4000, blank=True, null=True)
    genre = models.CharField(max_length=4000, blank=True, null=True)
    poster_link = models.CharField(max_length=1000, blank=True, null=True)
    netflix = models.IntegerField(blank=True, null=True)
    disneyplus = models.IntegerField(blank=True, null=True)
    wavve = models.IntegerField(blank=True, null=True)
    watcha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watcha'


class Wavve(models.Model):
    title = models.CharField(max_length=4000, blank=True, null=True)
    opening_date = models.CharField(max_length=1000, blank=True, null=True)
    just_rating = models.CharField(max_length=1000, blank=True, null=True)
    imdb_rating = models.CharField(max_length=1000, blank=True, null=True)
    runtime = models.CharField(max_length=500, blank=True, null=True)
    synopsis = models.CharField(max_length=4000, blank=True, null=True)
    director = models.CharField(max_length=1000, blank=True, null=True)
    actors = models.CharField(max_length=4000, blank=True, null=True)
    genre = models.CharField(max_length=4000, blank=True, null=True)
    poster_link = models.CharField(max_length=1000, blank=True, null=True)
    netflix = models.IntegerField(blank=True, null=True)
    disneyplus = models.IntegerField(blank=True, null=True)
    wavve = models.IntegerField(blank=True, null=True)
    watcha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wavve'