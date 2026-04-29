
from django.conf.urls.i18n import i18n_patterns, set_language
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 🔥 BU TASHQARIDA BO‘LADI
    path('set-language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('news/', include('news.urls')),
    path('rezidents/', include('rezidents.urls')),
    path('contact/', include('contact.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)