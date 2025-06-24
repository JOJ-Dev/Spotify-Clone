from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    model = Song
    fields = ['id', 
              'title',
              'artist',
              'album',
              'duration',
              'release_date',
              'cover_image',
              'lyrics',
              'genre',
              'popularity',
              'explicit',
              'file_url',
              ]
