import storage
import random
from classes.place import Place
from functions.search import binary_search
from functions.type_validation import is_integer
from functions import generate


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
        booked_place.reserve_room(place_data)

    @staticmethod
    def make():
        # allows user to select a place to book,

        choice = Place.let_user_select("Enter the number of the place you want to book:\n", Place.show_all)
        place_data = choice['sel_place']

        if int(place_data['available_rooms']) < 1:
            print(f"*{place_data['name'].upper()}* is fully booked!")
            Booking.make()
            return

        print(f"You have selected *{place_data['name'].upper()}*")

        # to generate booking id
        booking_id = generate.db_id('bookings', 'booking_id')

        # to get booking duration and any special request from user
        booking_duration = input('Please enter the duration of your stay (1 night minimum, 30 nights maximum):\n')
        while not is_integer(booking_duration, num_range=[1, 30]):
            booking_duration = input("Enter a VALID NUMBER from 1 to 30")

        special_req = input("Please enter any special requests you might have or press enter to complete booking:\n")

        selected_place = Booking(booking_id)
        selected_place.add_to_db(booking_duration, place_data, special_req)

    @staticmethod
    def end():
        # prints a list of bookings, user enters number that corresponds to a booking and ends it, increasing rooms available by 1
        # initial prompt to prepare the user

        choice = Place.let_user_select("Please enter the number of the booking you want to remove:\n", Booking.show_all)
        selected_booking = choice['sel_place']

        confirmation = input(f"Are you sure you want to end this booking for {selected_booking['accom_name'].upper()}? (Y/N)")
        if confirmation.lower() == 'y':
            storage.remove_data('bookings', key='booking_id', value=selected_booking['booking_id'])
            place = Place(selected_booking['accom_name'])
            place.unreserve_room()

    @staticmethod
    def show_all(show_end_booking_opt=False):
        # show_booking_opt=true will add a number and a prompt to the accommodation prints for user to enter and book that accommodation
        bookings = storage.load_data('bookings')
        current_index = 0
        for i in bookings:
            Booking._print(i, special_line=f"*[Enter {current_index + 1} to end this booking]*" if show_end_booking_opt else None)
            current_index += 1

        return bookings

    @staticmethod
    def _print(booking, special_line=None):
        print(f"*{booking['accom_name'].upper()}*")
        print(f"booking id: {booking['booking_id']}")
        print(f"duration: {booking['duration']} day(s)")
        print(f"special request: '{booking['special_req']}'")
        if special_line is not None:
            print(f"{special_line}")

        print("")
