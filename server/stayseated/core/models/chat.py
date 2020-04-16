from django.contrib.postgres.fields import JSONField
from django.db import models


class ChatEvent(models.Model):
    id = models.BigIntegerField(
        primary_key=True
    )  # Not using auto-increment since it doesn't give a 100% guarantee on monotony
    event_id = models.CharField(max_length=200, db_index=True)  # our global "event"
    channel = models.CharField(max_length=300, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=200)
    sender = models.ForeignKey("User", null=True, blank=True, on_delete=models.SET_NULL)
    content = JSONField()