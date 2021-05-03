class CreateFeedbackDto:
    customer_id: int
    message: str


class EditFeedbackDto:
    id: int
    customer_id: int
    message: str


class ListFeedbackDto:
    id: int
    customer_id: int
    message: str


class FeedbackDetailsDto:
    id: int
    customer_id: int
    message: str