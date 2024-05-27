
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='users/login/', permanent=False)),
    path('users/', include('users.urls', namespace='users')),
    path('people/', include('people.urls', namespace='people')),
    path('houses/', include('houses.urls', namespace='houses')),
    path('companies/', include('companies.urls', namespace='companies')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
