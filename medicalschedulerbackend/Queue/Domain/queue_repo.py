from abc import ABC, abstractmethod


class IQueueRepository(ABC):
    @abstractmethod
    def createQueue(self, patient_id:int):pass

    @abstractmethod
    def updateQueue(self, queue_id:int, status:int):pass

    @abstractmethod
    def deleteQueue(self, queue_id:int):pass

    @abstractmethod
    def assignPatientToDoctor(self, queue_id:int, doctor_id:int):pass

    @abstractmethod
    def assignPatientToDepartment(self, queue_id:int, department:str):pass

    @abstractmethod
    def getQueue(self, queue_id:int):pass

    @abstractmethod
    def getQueues(self):pass