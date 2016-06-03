from django.conf.urls import include, url
from django.contrib import admin

import app.views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('polls.urls')),
]