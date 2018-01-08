from rest_framework.decorators import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_417_EXPECTATION_FAILED, HTTP_404_NOT_FOUND, \
    HTTP_201_CREATED
from utils import mapper
from .serializer import MatchSerializer, MatchStatusSerializer, BetSerializer, CommentSerializer, \
    ScoreDetailSerializer
from .models import Match, MatchStatus, ScoreDetail, Bet, Comment
import logging


class MatchAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Match
    serializer = MatchSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url : http://localhost/match/match-detail/?match=<match_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            if query_params is False:
                admin_obj = self.model.objects.all()
                match_serializer = self.serializer(admin_obj, many=True)
                return Response(data=match_serializer.data, status=HTTP_200_OK)
            query_set = self.model.objects.filter(**query_params)
            match_serializer = self.serializer(query_set, many=True)
            return Response(data=match_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/match/match-detail/
        data schema : refer Match MODEL
        :param request:
        :return:
        """
        try:
            match_data = request.data
            match_serializer = self.serializer(data=match_data)
            if match_serializer.is_valid():
                match_serializer.save()
                return Response(data=match_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/match/match-detail/?match=<match_id>
        json_data required
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
        DELETE url: http://localhost/match/match-detail/?match=<match_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)


class ScoreAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = ScoreDetail
    serializer = ScoreDetailSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/match/match-score/?match=<match_id> or player=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            query_set = self.model.objects.filter(**query_params)
            score_serializer = self.serializer(query_set, many=True)
            return Response(data=score_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/match/match-score/
        data schema : refer ScoreDetail MODEL
        :param request:
        :return:
        """
        try:
            score_data = request.data
            score_detail_serializer = self.serializer(data=score_data, many=True)
            if score_detail_serializer.is_valid():
                score_detail_serializer.save()
                return Response(data=score_detail_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/match/match-score/?match=<match_id>&player=<player_id>
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
        DELETE url: http://localhost/match/match-score/?match=<match_id>&player=<player_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)


class MatchStatusAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = MatchStatus
    serializer = MatchStatusSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/match/match-status/?match=<match_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            query_set = self.model.objects.filter(**query_params)
            match_status_serializer = self.serializer(query_set, many=True)
            return Response(data=match_status_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/match/match-status/
        data schema : refer MatchStatus Model
        :param request:
        :return:
        """
        try:
            match_status_data = request.data
            match_status_serializer = self.serializer(data=match_status_data, many=True)
            if match_status_serializer.is_valid():
                match_status_serializer.save()
                return Response(data=match_status_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/match/match-status/?match=<match_id>
        data schema: MatchStatus MODEL
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
        DELETE url: http://localhost/match/match-status/?match=<match_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)


class BetAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Bet
    serializer = BetSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/match/match-bet-detail/match=<match_id>
        :param request:
        :return:
        """
        try:
            username = request.user.username
            query_params = mapper.re_map_query_params(request.params)
            if query_params is False:
                query_set = self.model.objects.filter(username=username)
            else:
                query_set_object = self.model.objects.get(username=username)
                query_set = query_set_object.filter(**query_params)
            bet_serializer = self.serializer(query_set, many=True)
            return Response(data=bet_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/match/match-bet-detail/
        data schema : refer Bet MODEL
        :param request:
        :return:
        """
        try:
            bet_data = request.data
            bet_serializer = self.serializer(data=bet_data, many=True)
            if bet_serializer.is_valid():
                bet_serializer.save()
                return Response(data=bet_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def delete(self, request):
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)


class CommentAPI(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    model = Comment
    serializer = CommentSerializer

    def _err_log(self, request_type):
        return "%s %s EXCEPTION REACHED" % (self.__class__.__name__, request_type)

    def get(self, request):
        """
        GET url: http://localhost/match/match-comment/?match=<match_id>or id=<comment_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            query_set = self.model.objects.filter(**query_params)
            comment_serializer = self.serializer(query_set, many=True)
            return Response(data=comment_serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        POST url: http://localhost/match/match-comment/
        data schema : refer Comment MODEL
        :param request:
        :return:
        """
        try:
            comments = request.data
            comment_serializer = self.serializer(data=comments, many=True)
            if comment_serializer.is_valid():
                comment_serializer.save()
                return Response(data=comment_serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logging.error("%s %s" % (self._err_log("GET"), e))
        return Response(status=HTTP_417_EXPECTATION_FAILED)

    def put(self, request):
        """
        PUT url: http://localhost/match/match-comment/?id=<comment_id>
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
        DELETE url: http://localhost/match/match-comment/?id=<comment_id>
        :param request:
        :return:
        """
        try:
            query_params = mapper.re_map_query_params(request.query_params)
            self.model.objects.filter(**query_params).delete()
        except Exception as e:
            logging.error("%s %s" % (self._err_log("DELETE"), e))
        return Response(status=HTTP_404_NOT_FOUND)
