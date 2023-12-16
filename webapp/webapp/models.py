from django.db import models

class Puzzle(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    FEN = models.CharField(max_length=200)
    moves = models.CharField(max_length=200)
    rating = models.IntegerField()
    rating_dev = models.IntegerField()
    popularity = models.IntegerField()
    Nb_plays = models.IntegerField()
    themes = models.CharField(max_length=200)
    game_url = models.CharField(max_length=200)
    openning_tags = models.CharField(max_length=200)