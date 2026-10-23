from hotel.rooms import (
    load_rooms,
    save_rooms,
    show_rooms,
    get_available_rooms,
    find_room_by_id,
    update_room_status,
)

ROOMS_FILE = "data/rooms.json"
BOOKINGS_FILE = "data/bookings.json"


def main():
    print("Hello from hotelbooking!")


if __name__ == "__main__":
    main()
