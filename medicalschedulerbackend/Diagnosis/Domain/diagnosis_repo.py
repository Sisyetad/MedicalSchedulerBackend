from abc import ABC, abstractmethod


class IDiagnosisRepository(ABC):
    @abstractmethod
    def createDiagnosis(self, diagnosis_name:str, severity_level:int, related_symptomes:str, clinical_notes:str, patient_id:int, doctor_id:int, medication:str):pass

    @abstractmethod
    def updateDiagnosis(self, diagnosis_id:int, severity_level:str, related_symptomes:str, clinical_notes:str, doctor_id:int, medication:str, updation_reason:str):pass

    @abstractmethod
    def getDiagnosis(self, diagnosis_id:int):pass

    @abstractmethod
    def getDiagnoses(self, patient_id):pass

    @abstractmethod
    def verify_vissiblity(self, diagnosis_id:int):pass

    @abstractmethod
    def displayHistory(self, diagnosis_id):pass

    @abstractmethod
    def updateDiagnosisStatus(self, diagnosis_id, diagnosis_status):pass