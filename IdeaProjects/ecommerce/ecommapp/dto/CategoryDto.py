class CreateCategoryDto:
    name: str
    parent_id: int


class EditCategoryDto:
    id: int
    name: str
    parent_id: int


class ListCategoryDto:
    id: int
    name: str
    parent_id: int


class CategoryDetailsDto:
    id: int
    name: str
    parent_id: int
