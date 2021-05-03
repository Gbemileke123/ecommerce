from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group
from ecommapp.dto.CommonDto import SelectOptionDto
from ecommapp.dto.AdminDto import CreateAdminDto, EditAdminDto, ListAdminDto, AdminDetailsDto
from ecommapp.models import Admin


class AdminRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an admin object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateAdminDto):
        """Create a admin object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, admin_id: int, model: EditAdminDto):
        """Update admin object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAdminDto]:
        """Gets list of admin"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, admin_id: int):
        """Deletes admin"""
        raise NotImplementedError

    @abstractmethod
    def get(self, admin_id: int):
        """Gets a single admin"""
        raise NotImplementedError


class DjangoORMAdminRepository(AdminRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        admin = Admin.objects.values("id", "user__last_name")
        return [SelectOptionDto(a["id"], a["last_name"]) for a in admin]

    def create(self, model: CreateAdminDto):
        admin = Admin()
        admin.contact_id = model.contact_id
        admin.job_title = model.job_title

        # create the user
        user = User.objects.create_user(model.username, model.password)
        user.user_first_name = model.user_first_name
        user.user_last_name = model.user_last_name
        user.save()

        admin.user = user
        admins = Group.objects.get(name='Admin')
        user.groups.add(admins)

        admin.save()

    def edit(self, admin_id: int, model: EditAdminDto):
        try:
            admin = Admin.objects.get(id=admin_id)
            admin.user_first_name = model.user_first_name
            admin.user_last_name = model.user_last_name
            admin.contact_id = model.contact_id
            admin.job_title = model.job_title
            admin.save()
        except Admin.DoesNotExist as a:
            message = "Admin information does not exist"
            print(message)
            raise a

    def list(self) -> List[ListAdminDto]:
        admin = list(Admin.objects.values("id",
                                          "user__first_name",
                                          "user__last_name",
                                          "contact_id",
                                          "job_title"))
        result: List[ListAdminDto] = []
        for a in admin:
            item = ListAdminDto()
            item.user_first_name = a["user_first_name"]
            item.user_last_name = a["user_last_name"]
            item.contact_id = a["contact_id"]
            item.job_title = a["job_title"]
            result.append(item)
        return result

    def delete(self, admin_id: int):
        try:
            admin = Admin.objects.get(id=admin_id)
            admin.delete()
        except Admin.DoesNotExist as a:
            message = "Admin information does not exist"
            print(message)
            raise a

    def get(self, admin_id: int):
        try:
            admin = Admin.objects.get(id=admin_id)
            result = AdminDetailsDto()
            result.id = admin.id
            result.user_first_name = admin.user.first_name
            result.user_last_name = admin.user.last_name
            result.contact_id = admin.contact_id
            result.job_title = admin.job_title
            return result
        except Admin.DoesNotExist as a:
            message = "Admin information does not exist"
            print(message)
            raise a


