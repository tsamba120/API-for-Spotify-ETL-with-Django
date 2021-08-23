# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DimAlbums(models.Model):
    album_id = models.TextField(primary_key=True)
    album_name = models.TextField(blank=True, null=True)
    artist = models.ForeignKey('DimArtists', models.DO_NOTHING, blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    total_tracks = models.IntegerField(blank=True, null=True)
    album_url = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'dim_albums'


class DimArtists(models.Model):
    artist_id = models.TextField(primary_key=True)
    artist_name = models.TextField(blank=True, null=True)
    artist_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_artists'


class DimSongs(models.Model):
    song_id = models.TextField(primary_key=True)
    song_name = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(DimArtists, models.DO_NOTHING, blank=True, null=True)
    album = models.ForeignKey(DimAlbums, models.DO_NOTHING, blank=True, null=True)
    duration_ms = models.IntegerField(blank=True, null=True)
    track_number = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    song_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_songs'


class SongPlays(models.Model):
    played_at = models.TextField(primary_key=True)
    song = models.ForeignKey(DimSongs, models.DO_NOTHING, blank=True, null=True)
    artist = models.ForeignKey(DimArtists, models.DO_NOTHING, blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song_plays'
