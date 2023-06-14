from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title