from custom_exceptions import TimeslotAlreadyBookedError


class Room:
    """Represents a classroom with its properties and booking schedule."""

    def __init__(self, room_no: str, building: str, capacity: int, booked_hours=None):
        self.room_no = room_no
        self.building = building
        self.capacity = capacity
        self.booked_hours = booked_hours if booked_hours else []

    def book(self, hour: int):
        """Book the room for a specific hour (0-23)."""
        if hour in self.booked_hours:
            raise TimeslotAlreadyBookedError(f"Hour {hour} is already booked.")
        if not (0 <= hour <= 23):
            raise ValueError("Hour must be between 0 and 23.")
        self.booked_hours.append(hour)
        print(f"Room {self.room_no} booked successfully for hour {hour}.")

    def is_free(self, hour: int):
        """Check if the room is free at a given hour."""
        return hour not in self.booked_hours

    def __str__(self):
        booked_str = ", ".join(map(str, sorted(self.booked_hours))) or "No bookings yet"
        return (f"\nRoom No: {self.room_no}\n"
                f"Building: {self.building}\n"
                f"Capacity: {self.capacity}\n"
                f"Booked Hours: {booked_str}\n")
