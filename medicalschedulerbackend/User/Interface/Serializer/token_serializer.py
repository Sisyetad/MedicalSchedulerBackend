# User/Interface/serializers/custom_token_serializer.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # ✅ Add custom claims here
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role.role_name if hasattr(user, 'role') else 'user'
        token['is_verified'] = user.is_active

        return token
