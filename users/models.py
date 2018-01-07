from django.db import models
from django.contrib.auth.models import User
from match.models import Match


# Create your models here.

class History(models.Model):
    user = models.ManyToManyField(User)
    match = models.ManyToManyField(Match)
