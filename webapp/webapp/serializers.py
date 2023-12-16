from rest_framework import serializers
from .models import Puzzle
class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = ["id","FEN","moves","rating","rating_dev","popularity","nb_plays","themes","game_url","opening_tags"]
