from django.db import models


class Profile(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
