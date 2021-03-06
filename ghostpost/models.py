from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    title = models.CharField(max_length=30)
    boolean = models.BooleanField()
    content = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
