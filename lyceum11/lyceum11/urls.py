from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('catalog/', include('catalog.urls')),
    url('about/', include('about.urls')),
    url('auth/', include('users.urls')),
    url('', include('homepage.urls'))
]
