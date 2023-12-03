import storage
from classes.place import Place


class Booking:
    def __init__(self, booking_id):
        self.booking_id = booking_id

    def add_to_db(self, duration, place_data, special_req=None):
        booking_data = {
            'booking_id': self.booking_id,
            'accom_name': place_data['name'],
            'duration': duration,
            'special_req': special_req,
        }
        storage.save_data(booking_data, 'bookings')

        # REDUCES ROOM AVAILABILITY BY 1
        booked_place = Place(place_data['name'])
        booked_place.add_booking(place_data)
