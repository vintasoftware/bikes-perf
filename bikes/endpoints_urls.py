from django.conf.urls import url

from .endpoints import BikeListAPIView


urlpatterns = [
    url(r'^bikes/$', BikeListAPIView.as_view(), name='bike-list'),
]
