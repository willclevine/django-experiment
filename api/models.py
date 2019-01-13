from django.db import models

# Create your models here.
from django.db.models import CASCADE

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class Rated(models.Model):
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    plays = models.IntegerField()
    finishes = models.IntegerField()
    skips = models.IntegerField()
    favs = models.IntegerField()
    deletions = models.IntegerField()
    duration = models.BigIntegerField()

    class Meta:
        abstract = True


class Tag(Rated):
    name = models.CharField(max_length=100)


class TagAssignment(models.Model):
    person = models.ForeignKey('Person', on_delete=CASCADE, related_name='person_tag')
    video = models.ForeignKey('Video', on_delete=CASCADE, related_name='video_tag')
    tag = models.ForeignKey('Tag', on_delete=CASCADE, related_name='tag')
    confidence = models.FloatField()


class Video(Rated):
    file_id = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    path = models.CharField(max_length=1000)
    size = models.IntegerField()
    length = models.IntegerField()
    resolution = models.IntegerField()
    people = models.ManyToManyField('Person', through='PersonAssignment')
    similarities = models.ManyToManyField('Video', through='SimilarityVideo')
    tags = models.ManyToManyField(Tag, through=TagAssignment)


class View(models.Model):
    start = models.FloatField()
    end = models.FloatField()
    video = models.ForeignKey(Video, on_delete=CASCADE)


class Person(Rated):
    name = models.CharField(max_length=100)
    similarities = models.ManyToManyField('Person', through='Similarity')
    videos = models.ManyToManyField(Video, through='PersonAssignment')
    tags = models.ManyToManyField(Tag, through=TagAssignment)


class PersonAssignment(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE)
    video = models.ForeignKey(Video, on_delete=CASCADE)
    confidence = models.FloatField()


class Similarity(models.Model):
    person_1 = models.ForeignKey(Person, on_delete=CASCADE, related_name='person_1')
    person_2 = models.ForeignKey(Person, on_delete=CASCADE, related_name='person_2')
    feature = models.CharField(max_length=100)


class SimilarityVideo(models.Model):
    video_1 = models.ForeignKey(Video, on_delete=CASCADE, related_name='video_1')
    video_2 = models.ForeignKey(Video, on_delete=CASCADE, related_name='video_2')
    feature = models.CharField(max_length=100)
