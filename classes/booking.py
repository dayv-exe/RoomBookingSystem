import storage
from classes.place import Place
from functions.type_validation import is_integer
from functions import generate


class Booking:
    def __init__(self, booking_id):
        self.booking_id = booking_id

    def add_to_db(self, duration, place_data, special_req=None):
        booking_data = {  # creates new data
            'booking_id': int(self.booking_id),
            'accom_name': place_data['name'],
            'duration': int(duration),
            'special_req': special_req,
        }
        storage.save_data(booking_data, 'bookings')  # saves new data created to db

        # REDUCES ROOM AVAILABILITY BY 1
        booked_place = Place(place_data['name'])
        booked_place.reserve_room(place_data)

    @staticmethod
    def make():
        # allows user to select a place to book,

        if len(storage.load_data('places')) < 1:  # if there are no places in database yet
            print(f"There are no places available for booking!")
            return

        # gives users a list of places, then they can select which of the places they want to book
        choice = Place.let_user_select("Enter the number of the place you want to book:\n", Place.show_all)
        place_data = choice['sel_place']  # the data of the place user selected

        if int(place_data['available_rooms']) < 1:
            # if the rooms available in the places user selected is less than 1
            # allow user to select another place to book
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

        # save booking details to db
        selected_place = Booking(booking_id)
        selected_place.add_to_db(booking_duration, place_data, special_req)

    @staticmethod
    def end():
        # prints a list of bookings, user enters number that corresponds to a booking and ends it, increasing rooms available by 1
        # initial prompt to prepare the user

        if len(storage.load_data('bookings')) < 1:
            # if there are no bookings in database yet
            print(f"There are no bookings to end!")
            return

        # allow user to select booking that they want to end
        choice = Place.let_user_select("Please enter the number of the booking you want to remove:\n", Booking.show_all)
        selected_booking = choice['sel_place']

        confirmation = input(f"Are you sure you want to end this booking for {selected_booking['accom_name'].upper()}? (Y/N)")  # get confirmation
        if confirmation.lower() == 'y':
            # remove booking from database
            storage.remove_data('bookings', key='booking_id', value=selected_booking['booking_id'])  # remove data from bookings where key = booking_id and value = selected_booking_id

            # gets the place that was booked and add 1 back to the number of rooms available since previous booking that has ended
            place = Place(selected_booking['accom_name'])
            place.unreserve_room()

    @staticmethod
    def show_all(show_end_booking_opt=False):
        # show_booking_opt=true will add a number and a prompt to the accommodation prints for user to enter and book that accommodation
        bookings = storage.load_data('bookings')
        if len(bookings) < 1:
            # if there are no bookings in db
            print(f"There are no bookings yet!")
            return

        current_index = 0
        for i in bookings:
            # show all bookings in db
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
