from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    pred_label_text = models.CharField(max_length=200, default='')
    pred_label_json = models.JSONField()
    # pred_label_code = models.CharField(max_length=200)
    pred_date = models.DateTimeField("date publish", default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Feedback(models.Model):
    feedback_txt = models.CharField(max_length=1000)
    feedback_date = models.DateTimeField("date publish")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
