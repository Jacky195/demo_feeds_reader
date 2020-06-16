from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url('feed/', include('api.admin.urls_feed'))
]