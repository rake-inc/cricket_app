from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'match-detail/$', views.MatchAPI.as_view()),
    url(r'match-score/$', views.ScoreAPI.as_view()),
    url(r'match-status/$', views.MatchStatusAPI.as_view()),
    url(r'match-status/$', views.MatchStatusAPI.as_view()),
    url(r'match-bet-detail/$', views.BetAPI.as_view()),
    url(r'match-comment/$', views.CommentAPI.as_view()),
]
