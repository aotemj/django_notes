from django.db import models


# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=timezone.now)
