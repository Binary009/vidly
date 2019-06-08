from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    # class-attr
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rates = models.FloatField()
    # associate each movie to a genre
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
