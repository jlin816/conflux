from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    # Examples:
    url(r'^setPlaid/', set_plaid_acct.as_view(), name='setacct'),
    url(r'^forceUpdatePlaid/', force_update_plaid_info.as_view(), name='forceupdate'),
    url(r'^user/', get_user_data.as_view(), name='userdata'),
    url(r'^business/transactions/', get_business_transactions.as_view(), name='transactions'),
    url(r'^transactions/rate/', rate_transaction.as_view(), name='rate_transactions'),

    # url(r'^$', 'hyppe.views.home', name='home'),
    # url(r'^/', include('main.urls')),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    # url(r'^admin/', include(admin.site.urls)),
]
