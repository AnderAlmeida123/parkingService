from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from django.urls import path

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
