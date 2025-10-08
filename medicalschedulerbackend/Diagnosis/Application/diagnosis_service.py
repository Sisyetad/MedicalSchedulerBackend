from django.core.exceptions import ValidationError

from Diagnosis.Domain.diagnosis_repo import IDiagnosisRepository


class DiagnosisService:
    def __init__(self, repository:IDiagnosisRepository):
        self.repository = repository
    
    def createDiagnosis(self, diagnosis_name, severity_level, related_symptomes, clinical_notes, patient_id, doctor_id, medication):
        try:
            return self.repository.createDiagnosis(diagnosis_name=diagnosis_name, severity_level=severity_level, related_symptomes=related_symptomes, clinical_notes=clinical_notes, patient_id=patient_id, doctor_id=doctor_id, medication=medication)
        except Exception as e:
            raise Exception(str(e))
    
    def updateDiagnosis(self, diagnosis_id, severity_level, related_symptomes, clinical_notes, doctor_id, medication, updation_reason):
        try:
            return self.repository.updateDiagnosis(diagnosis_id=diagnosis_id, severity_level=severity_level, related_symptomes=related_symptomes, clinical_notes=clinical_notes, doctor_id=doctor_id, medication=medication, updation_reason=updation_reason)
        except Exception as e:
            raise Exception(str(e))
        
    def getDiagnoses(self, patient_id):
        return self.repository.getDiagnoses(patient_id=patient_id)
    
    def getDiagnosis(self, diagnosis_id):
        try:
            return self.repository.getDiagnosis(diagnosis_id=diagnosis_id)
        except ValidationError as e:
            raise ValidationError(str(e))
    
    def verify_vissiblity(self, diagnosis_id):
        try:
            return self.repository.verify_vissiblity(diagnosis_id=diagnosis_id)
        except Exception as e:
            raise Exception(str(e))
        
    def displayHistory(self, diagnosis_id):
        try:
            return self.repository.displayHistory(diagnosis_id=diagnosis_id)
        except Exception as e:
            raise Exception(str(e))
        
    def updateDiagnosisStatus(self, diagnosis_id, diagnosis_status):
        try:
            return self.repository.updateDiagnosisStatus(diagnosis_id=diagnosis_id, diagnosis_status=diagnosis_status)
        except Exception as e:
            raise Exception(str(e))