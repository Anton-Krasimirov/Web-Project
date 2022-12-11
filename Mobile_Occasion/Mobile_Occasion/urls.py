from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mobile_Occasion.accounts.urls')),
    path('accounts/', include('Mobile_Occasion.autos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
