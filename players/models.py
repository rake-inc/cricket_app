from django.db import models
from postgres.db_config import MATCH_MODEL, TEAM_MODEL, PLAYER_MODEL


class Player(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Skill(models.Model):
    wickets = models.IntegerField()
    zeroes = models.IntegerField()
    ones = models.IntegerField()
    twos = models.IntegerField()
    threes = models.IntegerField()
    fours = models.IntegerField()
    six = models.IntegerField()
    total_matches = models.IntegerField()
    player = models.ForeignKey(Player)


class Stat(models.Model):
    batting_average = models.FloatField()
    bowling_average = models.FloatField()
    player = models.ForeignKey(Player)


class PlayerMatch(models.Model):
    player = models.ForeignKey(PLAYER_MODEL)
    match = models.ForeignKey(MATCH_MODEL)
    team = models.ForeignKey(TEAM_MODEL)
