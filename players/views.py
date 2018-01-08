from rest_framework.decorators import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_417_EXPECTATION_FAILED, HTTP_404_NOT_FOUND, \
    HTTP_201_CREATED
from utils import mapper
from .serializer import PlayerSerializer, SkillSerializer, StatSerializer, PlayerMatchSerializer
from .models import Player, Skill, Stat, PlayerMatch
import logging
from utils.metrics import CalculateStats
from postgres import fields


# Create your views here.

class PlayerDetailAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Player
    dependent_serializer = StatSerializer
    serializer = PlayerSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def _get_player_id(self, player_data_dict, player_name):
        player_id = self.model.objects.only(fields.PK).get(name=player_name).id
        player_data_dict[fields.PLAYER_ID] = player_id
        return player_data_dict

    def _get_player_data(self, raw_player_data):
        result = dict()
        result[fields.PLAYER_NAME] = raw_player_data[fields.PLAYER_NAME]
        result[fields.PLAYER_AGE] = raw_player_data[fields.PLAYER_AGE]
        return result

    def get(self, request):
        """
        GET url: http://localhost/players-detail/?id=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            if query_params is False:
                players_object = self.model.objects.all()
                player_serializer = self.serializer(players_object, many=True)
                return Response(data=player_serializer.data, status=HTTP_200_OK)
            query_set = self.model.objects.filter(**query_params)
            player_serializer = self.serializer(query_set, many=True)
            return Response(data=player_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/players-detail/
        data schema: Player MODEL
        :param request:
        :return:
        """
        try:
            raw_player_data = request.data
            processed_player_data = self._get_player_data(raw_player_data)
            player_serializer = PlayerSerializer(data=processed_player_data)
            if player_serializer.is_valid():
                player_serializer.save()
            player_data = self._get_player_id(raw_player_data, raw_player_data[fields.PLAYER_NAME])
            stats_data = CalculateStats(player_data)
            calculated_stat_data = stats_data.get_stats()
            stat_serializer = self.dependent_serializer(data=calculated_stat_data)
            if stat_serializer.is_valid():
                stat_serializer.save()
                return Response(data=player_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("POST"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def delete(self, request):
        """
        DELETE url: http://localhost/players-detail/?id=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)


class PlayerSkillAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Skill
    serializer = SkillSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/players-skill/?id=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            query_set = self.model.objects.filter(**query_params)
            skill_serializer = self.serializer(query_set, many=True)
            return Response(data=skill_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/players-skill/
        data schema: Skill MODEL
        :param request:
        :return:
        """
        try:
            skill_data = request.data
            skill_serializer = self.serializer(data=skill_data)
            if skill_serializer.is_valid():
                skill_serializer.save()
                return Response(skill_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("POST"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/players-skill/?id=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            modified_data = request.data
            self.model.objects.filter(**query_params).update(modified_data)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("PUT"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def delete(self, request):
        """
        DELETE url: http://localhost/players-detail/?id=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)


class PlayerStatAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Stat
    serializer = StatSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def put(self, request):
        """
        PUT url: http://localhost/players-stat/?id=<player_id>
        data schema: Stat MODEL
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            modified_data = request.data
            calculated_stats = CalculateStats(modified_data)
            calculated_stat_data = calculated_stats.get_stats()
            self.model.objects.filter(**query_params).update(calculated_stat_data)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("PUT"), e))
        return Response(status=HTTP_404_NOT_FOUND)


class PlayerMatchAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = PlayerMatch
    serializer = PlayerMatchSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/players-match/?id=<player_id>or match=<match_id> team = <team_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            query_set = self.model.objects.filter(**query_params)
            player_match_serializer = self.serializer(query_set, many=True)
            return Response(data=player_match_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/players-match/
        data schema: PlayerMatch MODEL
        :param request:
        :return:
        """
        try:
            player_match_data = request.data
            player_match_serializer = self.serializer(data=player_match_data)
            if player_match_serializer.is_valid():
                player_match_serializer.save()
                return Response(player_match_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("POST"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/players-match/?id=<player_id> or match=<match_id> or team=<team_id>
        data schema: PlayerMatch MODEL
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            modified_data = request.data
            self.model.objects.filter(**query_params).update(modified_data)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("PUT"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def delete(self, request):
        """
        DELETE url: http://localhost/players-match/?id=<player_id> or match=<match_id> or team=<team_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)
