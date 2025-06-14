
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
SpectacularAPIView,
SpectacularSwaggerView,
SpectacularRedocView
)

urlpatterns = [
    path('api/v1/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/v1/redoc/',SpectacularRedocView.as_view(), name='redoc'),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parking.urls')),
    path('api/v1/', include('vehicles.urls')),

    path('', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]
