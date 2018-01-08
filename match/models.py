from django.db import models
from django.contrib.auth.models import User
from postgres.db_config import PLAYER_MODEL, TEAM_MODEL, MATCH_MODEL
from django.contrib.postgres.fields import JSONField


class Match(models.Model):
    """
    team_details = JSONField()
    json format:
    {
        "start_time": "2017-01-05T18:30:00.000Z",
        "end_time": "2017-02-06T18:30:00.000Z",
        "team_details": {
            "team_a": <team_id>,
            "team_b": <team_id>
        }
    }
    """
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False, null=True)
    team_details = JSONField()

    def __str__(self):
        return str(self.pk)


class MatchStatus(models.Model):
    total_overs = models.FloatField()
    status = models.CharField(max_length=16)
    match = models.ForeignKey(Match)


class ScoreDetail(models.Model):
    score = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    match = models.ForeignKey(Match)
    player = models.ForeignKey(PLAYER_MODEL)
    zeroes = models.IntegerField(default=0)
    ones = models.IntegerField(default=0)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    six = models.IntegerField(default=0)


class Bet(models.Model):
    status = models.CharField(max_length=32)
    amount = models.IntegerField()
    user = models.ForeignKey(User)
    match = models.ForeignKey(Match)
    team = models.ForeignKey(TEAM_MODEL)


class Comment(models.Model):
    """
    players_details = JSONField()
    json format :
    {
        "bats_man":"<player_name>",
        "bowler":"<player_name>",
        "score":<int>,
        "action":"<zero> <ones> <twos> <threes> <fours> <fives> <six> <out>"
    }
    """
    over_no = models.FloatField()
    players_details = JSONField()
    team = models.ForeignKey(TEAM_MODEL)
    match = models.ForeignKey(MATCH_MODEL)
