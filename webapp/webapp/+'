from django.http import JsonResponse
from .models import Puzzle
from .serializers import PuzzleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def all_puzzles(request):
    if request.method == 'GET':
        puzzles = Puzzle.objects.all()
        serializer = PuzzleSerializer(puzzles, many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        serializer = PuzzleSerializer(data = request.data)
        if serializer.is_valild():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
