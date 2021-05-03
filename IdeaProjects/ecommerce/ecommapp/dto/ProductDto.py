class CreateProductDto:
    name: str
    price: float
    description: str
    product_image_id: int


class EditProductDto:
    id: int
    name: str
    price: float
    description: str
    product_image_id: int


class ListProductDto:
    id: int
    name: str
    price: float
    description: str
    product_image_id: int


class ProductDetailsDto:
    id: int
    name: str
    price: float
    description: str
    product_image_id: int
