from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url('admin/', include('api.urls_admin')),
    # url(r'^user/', include('api.urls_user'))
]