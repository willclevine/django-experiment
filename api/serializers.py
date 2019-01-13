from rest_framework import serializers

from api.models import Tag, Video, Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (
            'name',
            'similarities',
            'videos',
            'tags',
            'dislikes',
            'plays',
            'finishes',
            'skips',
            'favs',
            'deletions',
            'duration',
            'likes',
        )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
            'dislikes',
            'plays',
            'finishes',
            'skips',
            'favs',
            'deletions',
            'duration',
            'likes',
        )


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = (
            'file_id',
            'filename',
            'path',
            'size',
            'length',
            'resolution',
            'people',
            'similarities',
            'tags',
            'dislikes',
            'plays',
            'finishes',
            'skips',
            'favs',
            'deletions',
            'duration',
            'likes',
        )
