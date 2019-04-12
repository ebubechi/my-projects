from rest_framework import serializers
from django.contrib.auth.models import User
from music.models import Album, Song


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',)

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'album_logo', 'genre', 'is_favorite')


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('song_title ', 'audio_file', 'is_favorite',)
