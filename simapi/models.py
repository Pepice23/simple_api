from django.db import models


class Character(models.Model):
    karakter_name = models.CharField(max_length=32, unique=True, default="")
    karakter_faction = models.CharField(max_length=32, default="")
    karakter_gender = models.CharField(max_length=32, default="")
    karakter_race = models.CharField(max_length=32, default="")
    karakter_class = models.CharField(max_length=32, default="")

    def __str__(self):
        return self.karakter_name
