from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_datagrid import urls as datagrid_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(datagrid_urls)),
    # url(r'^(?:.*)/?$', include(datagrid_urls)),
]
