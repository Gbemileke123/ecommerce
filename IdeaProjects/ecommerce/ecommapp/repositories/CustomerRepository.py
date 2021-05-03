from abc import ABCMeta, abstractmethod
from typing import List, Dict

from django.contrib.auth.models import User, Group
from ecommapp.dto.CommonDto import SelectOptionDto
from ecommapp.dto.CustomerDto import CreateCustomerDto, EditCustomerDto, ListCustomerDto, CustomerDetailsDto
from ecommapp.models import Customer


class CustomerRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create a customer object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateCustomerDto):
        """Creates a customer object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditCustomerDto):
        """Updates a customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListCustomerDto]:
        """Gets list of a customer"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, customer_id: int):
        """Deletes a customer"""
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: int):
        """Gets a single customer"""
        raise NotImplementedError


class DjangoORMCustomerRepository(CustomerRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        customer = Customer.objects.values("id", "customer_id")
        return [SelectOptionDto(c["id"], c["customer_id"])for c in customer]

    def create(self, model: CreateCustomerDto):
        customer = Customer()
        customer.contact_id = model.contact_id

        # create the user
        user = User.objects.create_user(model.username, model.password)
        user.user_first_name = model.user_first_name
        user.user_last_name = model.user_last_name
        user.save()

        customer.user = user
        customers = Group.objects.get(name='Customer')
        user.groups.add(customers)

        customer.save()

    def edit(self, customer_id: int, model:EditCustomerDto):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.user_first_name = model.user_first_name
            customer.user_last_name = model.user_last_name
            customer.contact_id = model.contact_id
            customer.save()
        except Customer.DoesNotExist as c:
            message = "Customer does not exist"
            print(message)
            raise c

    def list(self) -> List[ListCustomerDto]:
        customer = list(Customer.objects.values("id",
                                                "user__first_name",
                                                "user__last_name",
                                                "contact_id",))
        result: List[ListCustomerDto] = []
        for c in customer:
            item = ListCustomerDto()
            item.id = c["id"]
            item.user_first_name = c["user__first_name"]
            item.user_last_name = c["user__last_name"]
            item.contact_id = c["contact_id"]
            result.append(item)
        return result

    def delete(self, customer_id: int):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
        except Customer.DoesNotExist as c:
            message = "Customer information does not exist"
            print(message)
            raise c

    def get(self, customer_id: int):
        try:
            customer = Customer.objects.get(id=customer_id)
            result = CustomerDetailsDto()
            result.id = customer.id
            result.contact_id = customer.contact_id
            result.user_first_name = customer.user_first_name
            result.user_last_name = customer.user_last_name
            return result
        except Customer.DoesNotExist as c:
            message = "Customer information does not exist"
            print(message)
            raise c
