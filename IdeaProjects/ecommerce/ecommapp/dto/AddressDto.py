class CreateAddressDto:
    state_id: int
    street: str
    city: str
    lga: str


class EditAddressDto:
    id: int
    state_id: int
    street: str
    city: str
    lga: str


class ListAddressDto:
    id: int
    state_id: int
    street: str
    city: str
    lga: str


class AddressDetailsDto:
    id: int
    state_id: int
    street: str
    city: str
    lga: str