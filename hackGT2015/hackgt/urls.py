from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'hyppe.views.home', name='home'),
    url(r'^api/', include('main.urls')),
    url(r'^api/login/', include('rest_social_auth.urls_token')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/user/', UserDetailView.as_view(), name="current_user"),
]
