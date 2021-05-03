from abc import ABCMeta, abstractmethod
from typing import List, Dict

from django.contrib.auth.models import User
from ecommapp.dto.CommonDto import SelectOptionDto
from ecommapp.dto.OrderDto import CreateOrderDto, EditOrderDto, ListOrderDto, OrderDetailsDto
from ecommapp.models import Order


class OrderRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates an order object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateOrderDto):
        """Create an order"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditOrderDto):
        """Updates an order object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListOrderDto]:
        """Gets the list of an order"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, order_id: int):
        """Deletes an order"""
        raise NotImplementedError

    @abstractmethod
    def get(self, order_id: int):
        """Gets a single order"""
        raise NotImplementedError


class DjangoORMOrderRepository(OrderRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        order = Order.objects.values("id", "order_id")
        return [SelectOptionDto(c["id"], c["order_status"]) for c in order]

    def create(self, model: CreateOrderDto):
        order = Order()
        order.customer_id = model.customer_id
        order.shipping_address_id = model.shipping_address_id
        order.order_status = model.order_status
        order.order_ref = model.order_ref
        order.save()

    def edit(self, id: int, model: EditOrderDto):
        try:
            order = Order.objects.get(id=id)
            order.customer_id = model.customer_id
            order.shipping_address_id = model.shipping_address_id
            order.order_status = model.order_status
            order.order_ref = model.order_ref
            order.save()
        except Order.DoesNotExist as orders:
            message = " This order does not exist"
            print(message)
            raise orders

    def list(self) -> List[ListOrderDto]:
        order = list(Order.objects.values("id",
                                          "customer_id",
                                          "shipping_address_id",
                                          "order_status",
                                          "order_ref"))
        result: List[ListOrderDto] = []
        for orders in order:
            item = ListOrderDto()
            item.id = orders["id"]
            item.customer_id = orders["customer_id"]
            item.shipping_address_id = orders["shipping_address_id"]
            item.order_status = orders["order_status"]
            item.order_ref = orders["order_ref"]
            result.append(item)
        return result

    def delete(self, order_id: int):
        try:
            order = Order.objects.get(id=order_id)
            order.delete(order_id)
        except Order.DoesNotExist as orders:
            message = " This order does not exist"
            print(message)
            raise orders

    def get(self, order_id: int):
        try:
            order = Order.objects.get(id=order_id)
            result = OrderDetailsDto()
            result.id = order.order_id
            result.customer_id = order.customer_id
            result.shipping_address_id = order.shipping_address_id
            result.order_status = order.order_status
            result.order_ref = order.order_ref
            return result
        except Order.DoesNotExist as orders:
            message = " This order does not exist"
            print(message)
            raise orders









