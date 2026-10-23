import json

def load_bookings(file_path):

    with open("bookings.json", "r") as file:
        bookings = json.load(file)

    return bookings


def save_bookings(file_path, bookings):

    with open("bookings.json", "w") as file:
        json.dump(bookings, file, indent=4)

    


def create_booking(room, guest_name):

    return {"room_id":room["room_id"], "name":guest_name}


def add_booking(bookings, booking):

    bookings.append(booking)


def show_bookings(bookings):

    for booking in bookings:

        print(booking)