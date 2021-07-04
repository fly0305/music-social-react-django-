from django.db import models
from django.conf import settings # you can use this for models instead of CustomUser
# assign User model as settings.AUTH_USER_MODEL

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='profile') 
    name = models.CharField(max_length=150)
    bio = models.TextField()
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    spotify = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)

# difference between ForeignKey and OneToOne field is that Foreign key is many-to-one relationships like Comment-Post
  #OneToOneField will return to ONLY one instance of QuerySet like Profile-RegisteredUser

class Genre(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='genre')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='genre') 
    genre = models.CharField(max_length=200, null=True)
    # might add ImageField

    def __str__(self):
        return '%s likes %s' % (self.user, self.genre)

class Artists(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='artists')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='artists') 
    artist = models.CharField(max_length=200, null=True)
    # might add ImageField

    def __str__(self):
        return '%s likes %s' % (self.user, self.artist)

class Tracks(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tracks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='tracks') 
    track = models.CharField(max_length=250, null=True)
    # might add ImageField

    def __str__(self):
        return '%s likes %s' % (self.user, self.track)

