import json


def load_rooms(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        rooms = json.load(file)
    return rooms


def save_rooms(file_path, rooms):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(rooms, file, indent=4, ensure_ascii=False)

def show_rooms(rooms):
    for room in rooms:
        status = "Available" if room["available"] else "Occupied"

        print(f'Room: {room["id"]} | Type: {room["type"]} | Price: {room["price"]} Ft | Status: {status}')

def get_available_rooms(rooms):
    available_rooms = []
    for room in rooms:
        if room["available"] == True:
            available_rooms.append(room)
    return available_rooms


def find_room_by_id(rooms, room_id):
    for room in rooms:
        if room["id"] == room_id:
            return room
    return None

def update_room_status(rooms, booking):
    for room in rooms:
        if room["id"] == booking["room_id"]:
            room["available"] = False
            return room
    return None