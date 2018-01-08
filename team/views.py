from rest_framework.decorators import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_417_EXPECTATION_FAILED, HTTP_404_NOT_FOUND, \
    HTTP_201_CREATED
from utils import mapper
from .serializer import TeamSerializer
from .models import Team
import logging


# Create your views here.

class TeamAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Team
    serializer = TeamSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/team-detail/?id=<team_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            query_set = self.model.objects.filter(**query_params)
            team_serializer = self.serializer(query_set, many=True)
            return Response(team_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/team-detail/
        data schema: Team MODEL
        :param request:
        :return:
        """
        try:
            team_data = request.data
            team_serializer = self.serializer(data=team_data)
            if team_serializer.is_valid():
                team_serializer.save()
                return Response(data=team_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("POST"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/team-detail/?id=<team_id>
        data schema: Team MODEL
        :param request:
        :return:
        """
        try:
            modified_data = request.data
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).update(**modified_data)
            return Response(data=modified_data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("PUT"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def delete(self, request):
        """
        DELETE url: http://localhost/team-detail/?id=<team_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
            return Response(status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)
