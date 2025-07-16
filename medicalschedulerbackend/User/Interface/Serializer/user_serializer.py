from rest_framework import serializers
from Role.Domain.role_entity import Role
from User.Domain.user_entity import UserEntity
from Role.Interface.role_serializer import RoleSerializer

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    role = RoleSerializer(required= False)
    access_token = serializers.CharField(read_only=True, required=False)
    refresh_token = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def validate(self, data):
        action = self.context.get('action')
        if action == 'signup':
            if not (data.get('username') and data.get('email') and data.get('password')):
                raise serializers.ValidationError("Username, email, and password are required for signup.")
        elif action == 'login':
            if not (data.get('email') and data.get('password')):
                raise serializers.ValidationError("Email and password are required for login.")
        elif action == 'logout':
            if not data.get('refresh_token'):
                raise serializers.ValidationError("Refresh token is required for logout.")
        return data

    def to_entity(self):
        return UserEntity(
            user_id=self.validated_data.get("user_id"),
            email=self.validated_data.get("email"),
            username=self.validated_data.get("username", ""),
            password=self.validated_data.get("password", ""),
            role=Role(
                role_id=self.validated_data.get("role", {}).get("role_id", 0),
                role_name=self.validated_data.get("role", {}).get("role_name", "")
            ),
            created_at=self.validated_data.get("created_at"),
            updated_at=self.validated_data.get("updated_at"),
            is_active=self.validated_data.get("is_active", False)
        )