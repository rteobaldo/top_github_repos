from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('github.urls')),
]

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
