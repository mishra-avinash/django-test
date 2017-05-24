from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from .views import EmployeeViewSet
from rest_framework import renderers
from . import views
from rest_framework.routers import DefaultRouter



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.ReactView.as_view(), name="react_app"),
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
