from django.contrib import admin
from django.urls import include, re_path
from django.conf import settings
from django.views import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('ACCOUNTS.urls')),
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^site_media/media/(?P<path>.*)$', include(static.serve),{'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^site_media/static/(?P<path>.*)$', include(static.serve),{'document_root': settings.STATIC_ROOT}),
]

