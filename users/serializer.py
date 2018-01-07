from rest_framework import serializers
from postgres import fields
from django.contrib.auth.models import User
from .models import History

USER_SERIALIZER_FIELDS = [
    fields.USERNAME,
    fields.FIRST_NAME,
    fields.LAST_NAME,
    fields.USER_PASSWORD,
    fields.USER_EMAIL,
    fields.IS_SUPERUSER,
    fields.IS_STAFF,
]

USER_ROLE_SERIALIZER_FIELD = [
    fields.IS_SUPERUSER,
]

HISTORY_SERIALIZER_FIELD = [
    fields.USER_ID,
    fields.MATCH_ID,
]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = USER_SERIALIZER_FIELDS

    def create(self, validated_data):
        """
        Creates auth_user object with password validation
        :param validated_data:
        :return:
        """
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data[fields.USER_PASSWORD])
        user.save()
        return user


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = USER_ROLE_SERIALIZER_FIELD


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = HISTORY_SERIALIZER_FIELD
