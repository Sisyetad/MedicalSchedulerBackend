from django.forms import ValidationError
from ..Domain.role_repo import IRoleRepository


class RoleService:
    def __init__(self, repository: IRoleRepository):
        self.repository =  repository

    def createRole(self, role_name: str):
        try:
            return self.repository.createRole(role_name= role_name)
        except ValidationError as e:
            return ValueError(str(e))
    
    def deleteRole(self, role_id):
        try:
            return self.repository.deleteRole(role_id= role_id)
        except ValidationError as e:
            return ValueError(str(e))
        
    def updateRole(self, role_id, role_name):
        try:
            return self.repository.updateRole(role_id= role_id, role_name= role_name)
        except ValidationError as e:
            return ValueError(str(e))
        
    def getAllRoles(self):
        try:
            return self.repository.getAllRoles()
        except ValidationError as e:
            return ValueError(str(e))
