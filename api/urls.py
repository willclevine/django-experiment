from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^rest/', include(router.urls)),
    url(r'^rest/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
