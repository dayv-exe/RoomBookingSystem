import storage


class Place:
    def __init__(self, name):
        self.name = name
        self.accom_type = 0
        self.address = None
        self.rooms = 0
        self.price = 0

    def add_to_db(self, accom_type, address, rooms, price):
        place_data = {
            'name': self.name,
            'accom_type': accom_type,
            'address': address,
            'available_rooms': rooms,
            'cost_per_night': price
        }
        storage.save_data(place_data, 'places')
