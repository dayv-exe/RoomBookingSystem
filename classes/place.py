import storage
from functions.search import binary_search
from functions.sort import binary_sort


class Place:
    def __init__(self, name):
        self.name = name

    def _place_data(self, accom_type, address, rooms, price):
        return {
            'name': self.name,
            'accom_type': accom_type,
            'address': address,
            'available_rooms': rooms,
            'cost_per_night': price
        }

    def add_to_db(self, accom_type, address, rooms, price):
        place_data = self._place_data(accom_type, address, rooms, price)
        storage.save_data(place_data, 'places')

    def _change_rooms_available(self, place_data, new_rooms_available):
        num = int(place_data['available_rooms'])
        updated_rooms_available = new_rooms_available

        new_place_data = self._place_data(place_data['accom_type'], place_data['address'], updated_rooms_available, place_data['cost_per_night'])
        storage.update_data('places', 'name', self.name, new_place_data)

    def add_booking(self, place_data):
        # reduces rooms available by 1
        num = int(place_data['available_rooms'])
        self._change_rooms_available(place_data, num - 1)

        print("Successfully completed booking!")

    def remove_booking(self):
        place_data = binary_sort(storage.load_data('places'), 'name')
        place_data = binary_search(place_data, self.name, 'name')
        # increases rooms available by 1
        num = int(place_data['available_rooms'])
        self._change_rooms_available(place_data, num + 1)

        print("\nSuccessfully removed booking!")
