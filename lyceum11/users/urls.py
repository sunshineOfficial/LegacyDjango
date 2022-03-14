from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^users/(?P<id>\d+)/$', views.user_detail),
    url(r'^users/$', views.user_list),
    url(r'^signup/$', views.signup),
    url(r'^profile/$', views.profile)
]