from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls import path, include

from diplom import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('my_profile/', include('myprofile.urls')),
    path('chat/', include('chat.urls')),
]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)