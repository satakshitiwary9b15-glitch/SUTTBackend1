from booking_system import BookingSystem
from custom_exceptions import (
    RoomNotFoundError,
    RoomAlreadyExistsError,
    TimeslotAlreadyBookedError
)


def main():
    system = BookingSystem()

    menu = """
CLASSROOM BOOKING SYSTEM:
1. Create a new room
2. Book a room
3. View room details
4. Find/filter rooms
5. Exit and save
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == '1':
                room_no = input("Enter room number: ").strip()
                building = input("Enter building name: ").strip()
                capacity = int(input("Enter capacity: ").strip())
                system.create_room(room_no, building, capacity)

            elif choice == '2':
                room_no = input("Enter room number to book: ").strip()
                hour = int(input("Enter hour to book (0-23): ").strip())
                system.book_room(room_no, hour)

            elif choice == '3':
                room_no = input("Enter room number to view: ").strip()
                system.view_room(room_no)

            elif choice == '4':
                print("\n--- Filter Options (press Enter to skip) ---")
                building = input("Building name: ").strip() or None
                min_capacity = input("Minimum capacity: ").strip()
                min_capacity = int(min_capacity) if min_capacity else None
                free_hour = input("Free at hour (0-23): ").strip()
                free_hour = int(free_hour) if free_hour else None

                matches = system.filter_rooms(building, min_capacity, free_hour)
                if matches:
                    print("\nAvailable Rooms:")
                    for r in matches:
                        print(r)
                else:
                    print("No rooms match the given criteria.")

            elif choice == '5':
                system.save_to_csv()
                print("Exiting program")
                break

            else:
                print("Invalid choice. Please try again.")

        except (RoomNotFoundError, RoomAlreadyExistsError, TimeslotAlreadyBookedError, ValueError) as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
