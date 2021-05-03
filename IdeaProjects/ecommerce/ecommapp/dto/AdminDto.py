class CreateAdminDto:
    username: str
    user_first_name: str
    user_last_name: str
    password: str
    contact_id: int
    job_title: str


class EditAdminDto:
    id: int
    user_first_name: str
    user_last_name: str
    contact_id: int
    job_title: str


class ListAdminDto:
    id: int
    user_first_name: str
    user_last_name: str
    contact_id: int
    job_title: str


class AdminDetailsDto:
    id: int
    user_first_name: str
    user_last_name: str
    contact_id: int
    job_title: str
