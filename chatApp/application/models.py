from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    messageText = models.CharField(max_length=1000)
    publishDate = models.DateTimeField(default=timezone.now)
    roomId=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.messageText

    def get_absolute_url(self):
        return reverse('home')


class ChatRoom(models.Model):
    roomName = models.CharField(max_length=120)
# Create your models here.
