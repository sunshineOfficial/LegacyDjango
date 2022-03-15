from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.item_detail),
    url(r'^$', views.item_list)
]