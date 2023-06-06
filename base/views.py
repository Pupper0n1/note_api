from django.shortcuts import render
from django.http import JsonResponse
from .models import Note
from api import serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
    routes = (
        '/api/routes/',
        '/api/list/',
        'api/note/<id>',
        '/api/create/',
        '/api/delete/<id>'

    )
    return Response(routes)

@api_view(['GET'])
def getList(request):
    stuff = Note.objects.all()
    # return JsonResponse('hello', safe=False)
    serialized = serializer.NoteSerializer(stuff, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getNote(request, pk):
    product = None
    pass


@api_view(['POST'])
def addNote(request):
    serialized = serializer.NoteSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)