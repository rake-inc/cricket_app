from .models import Team
from rest_framework import serializers
from postgres import fields

TEAM_SERIALIZER_FIELDS = [
    fields.TEAM_NAME,
    fields.TEAM_ORDER,
]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = TEAM_SERIALIZER_FIELDS
        model = Team
