from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .videos import descargar_video_twitter

# Create your views here.


@api_view(['GET'])
def twitter(request):
    url = request.data['url']
    enlace = descargar_video_twitter(url)
    return Response(enlace)