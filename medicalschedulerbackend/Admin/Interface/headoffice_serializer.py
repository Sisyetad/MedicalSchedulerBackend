from rest_framework import serializers

from Role.Interface.role_serializer import RoleSerializer

class HeadofficeSerializer(serializers.Serializer):
    headoffice_id = serializers.IntegerField(read_only = True)
    headoffice_name = serializers.CharField(required = False)
    email = serializers.EmailField()
    role = RoleSerializer()
    created_at = serializers.DateTimeField(read_only= True)
    updated_at = serializers.DateTimeField(read_only= True)
    is_active = serializers.BooleanField(read_only= True)

    def validate(self, data):
        action = self.context.get('action')
        if action == 'create':
            if not(data.get('headoffice_name') and data.get('email') and data.get('phone') and data.get('location')):
                raise serializers.ValidationError("Username, email, and password are required for signup.")
            
        return data