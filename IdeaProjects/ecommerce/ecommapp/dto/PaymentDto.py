class CreatePaymentDto:
    amount: float
    reference_number: str
    user_id: int
    order_id: int
    verified: bool


class EditPaymentDto:
    id: int
    amount: float
    reference_number: str
    user_id: int
    order_id: int
    verified: bool


class ListPaymentDto:
    id: int
    amount: float
    reference_number: str
    last_name: str
    order_id: int
    verified: bool


class PaymentDetailsDto:
    id: int
    amount: float
    reference_number: str
    user_id: int
    order_id: int
    verified: bool
