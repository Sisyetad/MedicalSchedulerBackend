from abc import ABC, abstractmethod

from Branch.Infrastructure.branch_model import BranchModel


class IBranchRepository(ABC):
    @abstractmethod
    def createBranch(self, branch_name, email, role_name:str, speciality, phone, location):pass

    @abstractmethod
    def deleteBranch(self, branch_id):pass

    @abstractmethod
    def updateBranch(self, branch_id, branch_name, speciality, location, phone): pass

    @abstractmethod
    def getBranch(self, branch_id): pass

    @abstractmethod
    def getBranches(self): pass

    @abstractmethod
    def getBranchByEmail(self, email)-> BranchModel: pass