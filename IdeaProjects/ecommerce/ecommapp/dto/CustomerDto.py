class CreateCustomerDto:
    username: str
    password: str
    user_first_name: str
    user_last_name: str
    contact_id: int


class EditCustomerDto:
    id: int
    user_first_name: str
    user_last_name: str
    contact_id: int


class ListCustomerDto:
    id: int
    user_first_name: str
    user_last_name: str
    contact_id: int


class CustomerDetailsDto:
    id: int
    user_first_name: str
    user_last_name: str
    contact_id: int
