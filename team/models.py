from django.db import models
from django.contrib.postgres.fields import JSONField


class Team(models.Model):
    """
    order = JSONField()
    json format:
    {
        "player_order":[
            <player_id>,
            <player_id>,
            ....
        ]
    }
    """
    name = models.CharField(max_length=64)
    order = JSONField()

    def __str__(self):
        return str(self.name)
