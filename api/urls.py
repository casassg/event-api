from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)