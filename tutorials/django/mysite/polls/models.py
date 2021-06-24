from datetime import timedelta

from django.db import models
from django.utils import timezone

__all__ = ["Question", "Choice"]


class Question(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.date >= now - timedelta(days=1)

    was_published_recently.admin_order_field = "date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

