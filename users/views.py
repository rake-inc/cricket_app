from .serializer import UserSerializer, UserRoleSerializer, HistorySerializer
from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_417_EXPECTATION_FAILED
import logging
from django.contrib.auth.models import User
from utils import mapper
from .models import History


# Create your views here.

class UserAPI(APIView):
    permission_classes = [AllowAny, ]

    model = User
    serializer = UserSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def post(self, request):
        try:
            user_data = request.data
            user_serializer = self.serializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
            return Response(user_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)


class UserDetailsAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = User
    serializer = UserRoleSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        try:
            username = request.user.username
            query_set = self.model.objects.filter(username=username)
            user_role_serializer = self.serializer(query_set, many=True)
            return Response(user_role_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_400_BAD_REQUEST)


class UserHistory(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = History
    serializer = HistorySerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        try:
            user_id = request.user.id
            query_set = self.model.objects.filter(user_id=user_id)
            user_history_serializer = self.serializer(query_set, many=True)
            return Response(user_history_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_400_BAD_REQUEST)
