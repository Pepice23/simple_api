from django.db import models


class Character(models.Model):
    karakter_name = models.CharField(max_length=32, unique=True, default="")
    race = models.CharField(max_length=32)
    cls = models.CharField(max_length=32)

    def __str__(self):
        return self.karakter_name
