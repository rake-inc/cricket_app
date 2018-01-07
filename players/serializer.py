from .models import Player, Skill, Stat, PlayerMatch
from rest_framework import serializers
from postgres import fields

PLAYER_SERIALIZER_FIELDS = [
    fields.PLAYER_NAME,
    fields.PLAYER_AGE,
]

SKILL_SERIALIZER_FIELDS = [
    fields.WICKET,
    fields.ZERO,
    fields.ONE,
    fields.TWO,
    fields.THREE,
    fields.FOURS,
    fields.SIX,
    fields.TOTAL_MATCHES,
    fields.PLAYER_ID,
]

STAT_SERIALIZER_FIELDS = [
    fields.BATTING_AVG,
    fields.BOWLING_AVG,
    fields.PLAYER_ID
]

PLAYER_MATCH_SERIALIZER_FIELDS = [
    fields.MATCH_ID,
    fields.TEAM_ID,

]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = PLAYER_SERIALIZER_FIELDS


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = SKILL_SERIALIZER_FIELDS


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = STAT_SERIALIZER_FIELDS


class PlayerMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMatch
        fields = PLAYER_MATCH_SERIALIZER_FIELDS
