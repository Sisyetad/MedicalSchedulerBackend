from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from User.Application.auth_service import AuthService
from User.Infrastructure.auth_repo_imp import DjangoAuthRepository
from User.Interface.Serializer.user_serializer import UserSerializer
from User.Application.token_utils import TokenUtils

from rest_framework.throttling import ScopedRateThrottle

class AuthView(APIView):
    service = AuthService(DjangoAuthRepository())

    throttle_scope = 'low_request'
    throttle_classes = [ScopedRateThrottle]
    
    def get_permissions(self):
        action = self.kwargs.get('action')
        if action in ['signup', 'login']:
            return [AllowAny()]
        elif action == 'logout':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_authenticators(self):
        action = self.kwargs.get('action')
        if action == 'logout':
            return [JWTAuthentication()]
        return super().get_authenticators()

    def post(self, request: Request, action: str = None):
        if action == 'signup':
            return self.signup(request)
        elif action == 'login':
            return self.login(request)
        elif action == 'logout':
            return self.logout(request)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


    def signup(self, request: Request):
        serializer = UserSerializer(data=request.data, context={'action': 'signup'})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            result = self.service.signUp(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                role_name=data['role']['role_name'],
                ip=TokenUtils.get_client_ip(request),
                device=TokenUtils.get_device_info(request),
                location=TokenUtils.get_location_from_ip(TokenUtils.get_client_ip(request))
            )

            return Response({
                "user": UserSerializer(result['user']).data,
                "access_token": result['access_token'],
                "refresh_token": result['refresh_token']
            }, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request: Request):
        serializer = UserSerializer(data=request.data, context={'action': 'login'})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            result = self.service.login(
                email=data['email'],
                password=data['password'],
                ip=TokenUtils.get_client_ip(request),
                device=TokenUtils.get_device_info(request),
                location=TokenUtils.get_location_from_ip(TokenUtils.get_client_ip(request))
            )

            return Response({
                "user": UserSerializer(result['user']).data,
                "access_token": result['access_token'],
                "refresh_token": result['refresh_token']
            }, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    def logout(self, request: Request):
        serializer = UserSerializer(data=request.data, context={'action': 'logout'})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            self.service.logout(data['refresh_token'])
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request: Request, action: str = None):
        return Response({"message": f"Send a POST request to perform '{action}'"}, status=200)
