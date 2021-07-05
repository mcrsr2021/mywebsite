from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  post_date = models.DateTimeField(auto_now_add=True)
  post_updated = models.DateTimeField(auto_now=True)
  body = models.TextField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('posts')