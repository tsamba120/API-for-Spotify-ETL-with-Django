from django.url import include, path
from .views import SongPlaysList, UniqueSongsList, UniqueArtistsList, UniqueAlbumsList

url_patterns = [
    path('song_plays/', SongPlaysList.as_view(), name='song-plays'),
    path('unique_songs/', UniqueSongsList.as_view(), name='unique-songs'),
    path('unique_artists/', UniqueArtistsList.as_view(), name='unique-artists'),
    path('unique_albums/', UniqueAlbumsList.as_view(), name='unique-albums')
]