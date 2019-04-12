from django.urls import include,re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


# app_name = 'music'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^music/', include('music.urls')),
    re_path(r'^', include('music.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
