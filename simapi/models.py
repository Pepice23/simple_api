from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=32)
    race = models.CharField(max_length=32)
    cls = models.CharField(max_length=32)

    def __str__(self):
        return self.name
