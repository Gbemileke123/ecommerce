class CreateOrderDto:
    customer_id: int
    shipping_address_id: int
    order_status: bool
    order_ref: str
    
    
class EditOrderDto:
    id: int
    customer_id: int
    shipping_address_id: int
    order_status: bool
    order_ref: str
    

class ListOrderDto:
    id: int
    customer_id: int
    shipping_address_id: int
    order_status: bool
    order_ref: str


class OrderDetailsDto:
    id: int
    customer_id: int
    shipping_address_id: int
    order_status: bool
    order_ref: str
