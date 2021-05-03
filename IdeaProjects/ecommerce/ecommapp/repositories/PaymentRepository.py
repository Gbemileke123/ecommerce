from abc import ABCMeta, abstractmethod
from typing import List, Dict

from django.contrib.auth.models import User
from ecommapp.dto.PaymentDto import CreatePaymentDto, EditPaymentDto, ListPaymentDto, PaymentDetailsDto
from ecommapp.dto.CommonDto import SelectOptionDto
from ecommapp.models import Payment


class PaymentRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a payment object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreatePaymentDto):
        """Creates Payment Object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditPaymentDto):
        """Updates payment object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[SelectOptionDto]:
        """Gets list of payment object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, payment_id: int):
        """Deletes a payment object"""
        raise NotImplementedError

    @abstractmethod
    def get(self, payment_id: int):
        """Gets a single payment"""
        raise NotImplementedError


class DjangoORMPaymentRepository(PaymentRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        payment = Payment.objects.values("id", "payment_id")
        return [SelectOptionDto(pay["id"], pay["order_status"]) for pay in payment]

    def create(self, model: CreatePaymentDto):
        payment = Payment()
        payment.amount = model.amount
        payment.reference_number = model.reference_number
        payment.= model.
