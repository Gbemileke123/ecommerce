class CreateContactDto:
    address_id: int
    name: str
    phone: str
    lga: str


class EditContactDto:
    id: int
    address_id: int
    name: str
    phone: str
    lga: str


class ListContactDto:
    id: int
    address_id: int
    name: str
    phone: str
    lga: str


class ContactDetailsDto:
    id: int
    address_id: int
    name: str
    phone: str
    lga: str