from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participants = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name