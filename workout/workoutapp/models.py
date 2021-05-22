from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    def __str__(self):
        return self.event_name

class Content(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    weight = models.IntegerField(default=0)
    set_number = models.IntegerField(default=0)
    training_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.event)
