from django.urls import include
from django.conf.urls import url
from api.admin import views_feed

urlpatterns = [
    url(r'^$', views_feed.main)
]