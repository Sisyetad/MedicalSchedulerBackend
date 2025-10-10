from Queue.Domain.queue_repo import IQueueRepository


class QueueService:
    def __init__(self, repository:IQueueRepository):
        self.repository = repository

    def createQueue(self, patient_int:int):
        try:
            return self.repository.createQueue(patient_id=patient_int)
        except Exception as e:
            raise Exception(str(e))
        
    def updateQueue(self, queue_id:int, status:int):
        try:
            return self.repository.updateQueue(queue_id=queue_id, status=status)
        except Exception as e:
            raise Exception(str(e))
        
    def deleteQueue(self, queue_id:int):
        try:
            return self.repository.deleteQueue(queue_id=queue_id)
        except Exception as e:
            raise Exception(str(e))
        
    def assignPatientToDoctor(self, queue_id:int, doctor_id:int):
        try:
            return self.repository.assignPatientToDoctor(queue_id=queue_id, doctor_id=doctor_id)
        except Exception as e:
            raise Exception(str(e))
        
    def assignPatientToDepartment(self, queue_id:int, department:int):
        try:
            return self.repository.assignPatientToDepartment(queue_id=queue_id, department=department)
        except Exception as e:
            raise Exception(str(e))
        
    def getQueue(self, queue_id:int):
        try:
            return self.repository.getQueue(queue_id=queue_id)
        except Exception as e:
            raise Exception(str(e))
        
    def getQueues(self):
        try:
            return self.repository.getQueues()
        except Exception as e:
            raise Exception(str(e))