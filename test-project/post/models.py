from django.contrib.auth import get_user_model
from django.db import models


class PostManager(models.Manager):
    def new(self):
        return self.order_by('-date')


class Post(models.Model):
    objects = PostManager()
    author = models.ForeignKey(get_user_model(), blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def like_from_user(self, user):
        return self.likes.filter(author=user, state=True).last()


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), blank=False, null=False)
    post = models.ForeignKey(Post, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class LikeManager(models.Manager):
    def active(self):
        return self.filter(state=True)


class Like(models.Model):
    objects = LikeManager()
    author = models.ForeignKey(get_user_model(), blank=False, null=False)
    state = models.BooleanField(default=True)
    post = models.ForeignKey(
        Post,
        related_name='likes',
        blank=False,
        null=False
    )

    def change_state(self):
        self.state = False if self.state else True
        self.save()
