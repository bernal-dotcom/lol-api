from django.db import models

class Standing(models.Model):
    """
    Model representing a League of Legends standing.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


