from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    release_date = models.DateField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length = 100, blank=True, null=True)
    popularity = models.PositiveIntegerField(default=0)
    explicit = models.BooleanField(default=False)
    file_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

# Create your models here.
