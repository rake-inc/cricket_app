from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'create-user/$', views.UserAPI.as_view()),
    url(r'users-details/$', views.UserDetailsAPI.as_view()),
    url(r'users-history/$', views.UserHistory.as_view()),
]
