from django.shortcuts import render
from .models import SongPlays, DimSongs, DimArtists, DimAlbums
from rest_framework import generics
from .serializers import SongPlays_Serializer, DimSongs_Serializer, DimArtists_Serializer, DimAlbums_Serializer


class SongPlaysList(generics.ListAPIView):
    '''
    API endpoint that allows song plays, song_id, and artist_id to be viewed
    '''
    queryset = SongPlays.objects.all()
    serializer_class = SongPlays_Serializer