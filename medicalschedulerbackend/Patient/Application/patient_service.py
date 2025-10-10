from django.core.exceptions import ValidationError
from Patient.Domain.patient_repo import IPatientRepository


class PatientService:
    def __init__(self, repository: IPatientRepository):
        self.repository = repository

    def createPatient(self, full_name:str, email:str, phone:str, location:str, sex:str, birth_date, role_name:str, branch_name:str):
        try:
            return self.repository.createPatient(full_name=full_name, email=email, phone=phone, location=location, sex=sex, birth_date=birth_date, role_name=role_name, branch_name=branch_name)
        except ValidationError as e:
            raise ValidationError(str(e))
        
    def updatePatient(self, patient_id:int, full_name:str, email:str, phone:str, location:str, sex:str, birth_date):
        try:
            return self.repository.updatePatient(patient_id=patient_id, full_name=full_name, email=email, phone=phone, location=location, sex= sex, birth_date=birth_date)
        except ValidationError as e:
            raise ValidationError(str(e))
        
    def deletePatient(self,patient_id:int):
        try:
            return self.repository.delelePatient(patient_id=patient_id)
        except ValidationError as e:
            raise ValidationError(str(e))
        
    def getPatientByID(self, patient_id:int):
        try:
            return self.repository.getPatientByID(patient_id=patient_id)
        except ValidationError as e:
            raise ValidationError(str(e))
        
    def getPatients(self):
        try:
            return self.repository.getPatients()
        except ValidationError as e:
            raise ValidationError(str(e))