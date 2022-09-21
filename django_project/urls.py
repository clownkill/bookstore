from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('anything_but_admin/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),
    # Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debut__/', include(debug_toolbar.urls)),
    ] + urlpatterns
