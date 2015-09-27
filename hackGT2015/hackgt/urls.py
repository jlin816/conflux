from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'hyppe.views.home', name='home'),
    url(r'^/', include('main.urls')),
    # url(r'^api/user/', UserDetailView.as_view(), name="current_user"),
]
