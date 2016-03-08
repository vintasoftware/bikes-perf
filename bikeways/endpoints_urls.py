from django.conf.urls import url

from .endpoints import BikewayListAPIView, BikewayListAPIJSONView, \
    BikewayCategoryListAPIView, BikewayListSerpyAPIJSONView, \
    BikewayListNoSerializerAPIJSONView


urlpatterns = [
    url(r'^bikeways/$', BikewayListAPIView.as_view(), name='bikeway-list'),
    url(r'^bikeways/json/$', BikewayListAPIJSONView.as_view(), name='bikeway-list-json'),
    url(r'^bikeways/json/serpy/$', BikewayListSerpyAPIJSONView.as_view(), name='bikeway-list-serpy-json'),
    url(r'^bikeways/json/nothing/$', BikewayListNoSerializerAPIJSONView.as_view(), name='bikeway-list-nothing-json'),
    url(r'^bikeways-categories/$', BikewayCategoryListAPIView.as_view(), name='category-list')
]
