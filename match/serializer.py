from .models import Match, Bet, Comment, ScoreDetail, MatchStatus
from rest_framework import serializers
from postgres import fields

MATCH_SERIALIZER_FIELDS = [
    fields.MATCH_START_TIME,
    fields.MATCH_END_TIME,
    fields.TEAM_DETAILS,
]

BET_SERIALIZER_FIELDS = [
    fields.STATUS,
    fields.USER_ID,
    fields.TEAM_ID,
    fields.AMOUNT,
    fields.MATCH_ID,
]

COMMENT_SERIALIZER_FIELDS = [
    fields.OVER_NO,
    fields.TEAM_ID,
    fields.MATCH_ID,
    fields.PLAYER_DETAILS,
]

SCORE_DETAIL_FIELDS = [
    fields.SCORE,
    fields.TOTAL_WICKETS,
    fields.MATCH_ID,
    fields.PLAYER_ID,
]

MATCH_STATUS_SERIALIZER_FIELDS = [
    fields.TOTAL_OVER,
    fields.STATUS,
    fields.MATCH_ID,
]


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = MATCH_SERIALIZER_FIELDS


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = BET_SERIALIZER_FIELDS


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = COMMENT_SERIALIZER_FIELDS


class ScoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreDetail
        fields = SCORE_DETAIL_FIELDS


class MatchStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchStatus
        fields = MATCH_STATUS_SERIALIZER_FIELDS
