from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^users/(?P<id>\d+)/$', views.user_detail),
    url('users/', views.user_list),
    url('signup/', views.signup),
    url('profile/', views.profile)
]