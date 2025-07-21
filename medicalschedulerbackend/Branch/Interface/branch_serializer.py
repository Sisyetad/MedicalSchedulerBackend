from rest_framework import serializers
from Role.Interface.role_serializer import RoleSerializer
from Admin.Interface.headoffice_serializer import HeadofficeSerializer

class BranchSerializer(serializers.Serializer):
    branch_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    branch_name = serializers.CharField(required=False)
    role = RoleSerializer(required= False)
    phone = serializers.CharField(required=False)
    speciality = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    headoffice = HeadofficeSerializer(read_only= True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def validate(self, data):
        action = self.context.get('action')
        if action == 'create':
            required_fields = ['branch_name', 'email', 'phone', 'speciality', 'location', 'role']
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                raise serializers.ValidationError(f"Missing required fields for create: {', '.join(missing_fields)}")
        elif action == 'update':
            update_fields = ['branch_name', 'phone', 'speciality', 'location']
            if not any(data.get(field) for field in update_fields):
                raise serializers.ValidationError("At least one field must be provided for update.")
        return data