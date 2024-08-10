from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from noteapp.models import Note
from noteapp.serializers import NoteSerializer

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        note = Note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
