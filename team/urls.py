from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'team-detail/$', views.TeamAPI.as_view()),
]
