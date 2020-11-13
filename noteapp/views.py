from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/notes-list/',
        'List One': '/notes-list/<str:pk>/'
        'Create': '/notes-create/',
        'Update': '/notes-update/<str:pk>/',
        'Delete': '/notes-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def NoteList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def NoteListOne(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def NoteCreate(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def NoteUpdate(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def NoteDelete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note Deleted Successfully")
