from django.db import models

# Create your models here.
from django.utils import timezone


class Note(models.Model):
    note = models.CharField(max_length=70, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
	    return self.note