class RoomNotFoundError(Exception):
    """Raised when the room ID does not exist."""
    pass


class TimeslotAlreadyBookedError(Exception):
    """Raised when a user tries to book an already occupied hour."""
    pass


class RoomAlreadyExistsError(Exception):
    """Raised when trying to create a room that already exists."""
    pass
