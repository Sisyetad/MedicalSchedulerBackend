from rest_framework import serializers

from Doctor.Interface.doctor_serializer import DoctorSerializer
from Patient.Interface.patient_serializer import PatientSerializer

class QueueSerializer(serializers.Serializer):
    queue_id = serializers.IntegerField(read_only=True)
    patient_id = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    doctor_id = serializers.IntegerField(required=False)
    department = serializers.CharField(required=False)
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    def validate(self, data):
        action = self.context.get("action")
        if action == 'create':
            if not data.get("patient_id"):
                raise serializers.ValidationError(f"Missing required fields for create: patient_id")
        elif action == 'update':
            if not data.get("status"):
                raise serializers.ValidationError("Give status for update.")
        elif action == 'partial_update':
            if not data.get('doctor_id') and not data.get('department'):
                raise serializers.ValidationError("Give either doctor_id or department for update.")
            
        return data