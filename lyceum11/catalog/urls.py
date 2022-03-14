from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.item_detail),
    url(r'^$', views.item_list)
]