from django.db import models
from login.models import *

# Create your models here.
class Message(models.Model):
  message = models.TextField()
  author = models.ForeignKey(User, related_name="author_messages", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  Updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  comment = models.CharField(max_length=255)
  author = models.ForeignKey(User, related_name="author_comments", on_delete=models.CASCADE)
  message = models.ForeignKey(Message, related_name="post_comments", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  Updated_at = models.DateTimeField(auto_now=True)

