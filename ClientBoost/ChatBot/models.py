from django.db import models
from dataset_prepare.models import *
# Create your models here.


class Ad(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="ads")
    labels = models.ManyToManyField(ProblemLabel, related_name="ads")
    first_text = models.TextField(default="Buna")


class Context(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="contexts")
    data = models.JSONField(default=dict)


class Session(models.Model):
    external_id = models.IntegerField(default=0)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="sessions")
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class History(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="histories")
    text = models.JSONField(default=dict)
