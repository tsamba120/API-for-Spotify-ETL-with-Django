from rest_framework import serializers
from .models import SongPlays, DimSongs, DimArtists, DimAlbums

class SongPlays_Serializer(serializers.ModelSerializer):

    class Meta:
        model = SongPlays
        fields = ['played_at', 'song', 'artist', 'timestamp']

class DimSongs_Serializer(serializers.ModelSerializer):

    class Meta:
        model = DimSongs
        fields = ['song_id', 'song_name', 'artist', 'album', 'duration_ms', 'track_number', 'popularity', 'song_url']

class DimArtists_Serializer(serializers.ModelSerializer):

    class Meta:
        model = DimArtists
        fields = ['artist_id', 'artist_name', 'artist_url']

class DimAlbums_Serializer(serializers.ModelSerializer):

    class Meta:
        model = DimAlbums
        fields = ['album_id', 'album_name', 'artist', 'release_date', 'total_tracks', 'album_url']

