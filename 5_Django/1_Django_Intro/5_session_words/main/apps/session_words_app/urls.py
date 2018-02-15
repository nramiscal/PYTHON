from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^session_words/$', views.process),
    url(r'^clear$', views.clear)
]
