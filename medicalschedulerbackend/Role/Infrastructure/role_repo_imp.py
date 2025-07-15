from .role_model import RoleModel
from ..Domain.role_repo import IRoleRepository


class RoleRepository(IRoleRepository):
    def createRole(self, role_name):
        role_model = RoleModel.objects.create(role_name = role_name)
        return role_model.to_entity()
    
    def deleteRole(self, role_id):
        try:
            role = RoleModel.objects.get(pk = role_id)
            role.delete()
            return True
        except RoleModel.DoesNotExist:
            return False
    
    def updateRole(self, role_id, role_name):
        try:
            role = RoleModel.objects.get(pk = role_id)
            role.name = role_name
            return role.to_entity()
        except RoleModel.DoesNotExist:
            return ValueError("Invalid role ID.")
    
    def getAllRoles(self):
        return [role.to_entity() for role in  RoleModel.objects.all()]