from django.conf.urls import url

from .endpoints import BikewayListAPIView, BikewayListAPIJSONView, BikewayCategoryListAPIView


urlpatterns = [
    url(r'^bikeways/$', BikewayListAPIView.as_view(), name='bikeway-list'),
    url(r'^bikeways/json/$', BikewayListAPIJSONView.as_view(), name='bikeway-list-json'),
    url(r'^bikeways-categories/$', BikewayCategoryListAPIView.as_view(), name='category-list')
]
