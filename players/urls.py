from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'players-detail/$', views.PlayerDetailAPI.as_view()),
    url(r'players-skill/$', views.PlayerSkillAPI.as_view()),
    url(r'players-stats/$', views.PlayerStatAPI.as_view()),
    url(r'players-match/$', views.PlayerMatchAPI.as_view()),
]
