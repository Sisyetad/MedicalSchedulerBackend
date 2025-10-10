from abc import ABC, abstractmethod


class IPatientRepository(ABC):
    @abstractmethod
    def createPatient(self, full_name:str, email:str, phone:str, role_name:str, location:str,sex:str, birth_date, branch_name:str):pass

    @abstractmethod
    def updatePatient(self, patient_id:int, full_name:str, email:str, phone:str, location:str,sex:str, birth_date):pass

    @abstractmethod
    def delelePatient(self, patient_id:int):pass

    @abstractmethod
    def getPatients(self):pass

    @abstractmethod
    def getPatientByID(self, patient_id:int):pass