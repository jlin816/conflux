from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    # Examples:
    url(r'^raspiCoord/', setRaspiPos.as_view(), name='setpos'),
    url(r'^upload_data/', upload_data.as_view(), name='data'),
    url(r'^positions/', getpositions.as_view(), name='pos'),

    # url(r'^$', 'hyppe.views.home', name='home'),
    # url(r'^/', include('main.urls')),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    # url(r'^admin/', include(admin.site.urls)),
]
