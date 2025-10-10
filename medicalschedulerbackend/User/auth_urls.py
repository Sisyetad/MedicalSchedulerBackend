# medicalschedullerbackend/User/urls.py

from django.urls import path

from .Interface.View.auth_view import AuthView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<str:action>/', AuthView.as_view(), name='auth-action')
]