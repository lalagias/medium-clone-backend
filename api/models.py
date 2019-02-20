from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile",
        primary_key=True)
    bio = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="profileImages")

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_post")
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    text = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="postImages")

    # tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="author_comment")
    text = models.TextField(default="")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
