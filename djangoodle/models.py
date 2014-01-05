from django.db import models
import datetime
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time_of_creation = models.DateTimeField(default=datetime.datetime.now())
    email_of_creator = models.EmailField()

    def __unicode__(self):
        return self.name

class EventItem(models.Model):
    event = models.ForeignKey('Event')
    event_item_time = models.DateTimeField()
    event_item_name = models.CharField(max_length=100)

class Participant(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey('Event')
    time_of_authorization = models.DateTimeField(default=datetime.datetime.now())
    event_items = models.ManyToManyField('EventItem')

    def __unicode__(self):
        return self.name
        