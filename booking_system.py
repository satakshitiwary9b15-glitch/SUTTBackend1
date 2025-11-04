import csv
import os
from room import Room
from custom_exceptions import (
    RoomAlreadyExistsError,
    RoomNotFoundError,
    TimeslotAlreadyBookedError
)


class BookingSystem:
    """Handles all operations: room creation, booking, searching, saving, and loading."""

    def __init__(self, csv_filename="bookings_final_state.csv"):
        self.rooms = {}
        self.csv_filename = csv_filename
        self.load_from_csv()

    def create_room(self, room_no: str, building: str, capacity: int):
        if room_no in self.rooms:
            raise RoomAlreadyExistsError(f"Room '{room_no}' already exists.")
        self.rooms[room_no] = Room(room_no, building, capacity)
        print(f"Room '{room_no}' created successfully.")

    def book_room(self, room_no: str, hour: int):
        room = self.get_room(room_no)
        room.book(hour)

    def get_room(self, room_no: str) -> Room:
        if room_no not in self.rooms:
            raise RoomNotFoundError(f"Room '{room_no}' not found.")
        return self.rooms[room_no]

    def view_room(self, room_no: str):
        room = self.get_room(room_no)
        print(room)

    def filter_rooms(self, building=None, min_capacity=None, free_hour=None):
        results = []
        for room in self.rooms.values():
            if building and room.building != building:
                continue
            if min_capacity and room.capacity < min_capacity:
                continue
            if free_hour is not None and not room.is_free(free_hour):
                continue
            results.append(room)
        return results

    def save_to_csv(self):
        with open(self.csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["room_no", "building", "capacity", "booked_hours"])
            for room in self.rooms.values():
                hours_str = ";".join(map(str, sorted(room.booked_hours)))
                writer.writerow([room.room_no, room.building, room.capacity, hours_str])
        print(f"\nData saved to '{self.csv_filename}'.")

    def load_from_csv(self):
        if not os.path.exists(self.csv_filename):
            return
        with open(self.csv_filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                booked = [int(x) for x in row["booked_hours"].split(";") if x.strip()]
                self.rooms[row["room_no"]] = Room(
                    row["room_no"], row["building"], int(row["capacity"]), booked
                )
