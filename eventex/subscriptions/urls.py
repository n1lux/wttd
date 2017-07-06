from django.conf.urls import url
from eventex.subscriptions.views import new as new_view
from eventex.subscriptions.views import detail as detail_view

urlpatterns = [
    url(r'^$', new_view, name='new'),
    url(r'^([\w]{32})/$', detail_view, name='detail'),
]