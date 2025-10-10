from rest_framework import serializers
from Role.Interface.role_serializer import RoleSerializer

class PatientSerializer(serializers.Serializer):
    patient_id= serializers.IntegerField(read_only=True)
    full_name= serializers.CharField(required=False)
    email= serializers.EmailField(required=False)
    role= RoleSerializer(required=False)
    phone= serializers.CharField(required=False)
    location= serializers.CharField(required=False)
    sex = serializers.CharField(required=False)
    birth_date =serializers.DateTimeField(required=False)
    branch_name = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def validate(self, data):
        action = self.context.get('action')
        if action == 'create':
            required_fields = ['full_name', 'email', 'phone', 'role', 'location', 'sex', 'birth_date', 'branch_name']
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                raise serializers.ValidationError(f"Missing required fields for create: {', '.join(missing_fields)}")
        elif action == 'update':
            update_fields = ['full_name', 'email', 'phone', 'location', 'sex', 'birth_date', 'branch_name']
            if not any(data.get(field) for field in update_fields):
                raise serializers.ValidationError("At least one field must be provided for update.")
            
        return data