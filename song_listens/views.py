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


class UniqueSongsList(generics.ListAPIView):
    '''
    API endpoint that provides a list of unique songs played
    '''
    queryset = DimSongs.objects.all()
    serializer_class = DimSongs_Serializer


class UniqueArtistsList(generics.ListAPIView):
    '''
    API endpoint that provides a list of unique artists listened to
    '''
    queryset = DimArtists.objects.all()
    serializer_class = DimArtists_Serializer


class UniqueAlbumsList(generics.ListAPIView):
    '''
    API endpoint that provides a list of unique albums listened to
    '''
    queryset = DimAlbums.objects.all()
    serializer_class = DimAlbums_Serializer
 