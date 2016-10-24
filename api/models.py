import uuid

from django.db import models

EVENT_TYPES = [('essential', 'Essential'), ('food', 'Food'), ('events', 'Events'), ('talks', 'Talks')]


# Create your models here.

class Event(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()
    title = models.TextField()
    place = models.TextField()
    type = models.TextField(choices=EVENT_TYPES)
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ('begin',)
