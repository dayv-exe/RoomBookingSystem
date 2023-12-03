import random

import storage
from functions.places import show_all_places
from classes.place import Place
from functions.type_validation import is_integer
from classes.booking import Booking
from functions.search import binary_search
from functions.sort import binary_sort


def make_booking():
    # allows user to select a place to book,

    # initial prompt to prepare the user
    input("Press enter to see a list of places available to be booked, then enter the number of the place you want to book.")
    print("\n")

    places = show_all_places(show_booking_opt=True)
    selected_place = input('Enter the number of the place you want to book:\n')
    while is_integer(selected_place, num_range=[1, len(places)]) is False:
        selected_place = input('Enter a VALID NUMBER from the list of the place you want to book:\n')

    place_data = places[int(selected_place) - 1]

    if int(place_data['available_rooms']) < 1:
        print(f"*{place_data['name'].upper()}* is fully booked!")
        make_booking()

    print(f"You have selected *{place_data['name'].upper()}*")

    # to generate booking id
    booking_id = random.randint(1, 999999)
    while binary_search(storage.load_data('bookings'), search_term=booking_id, key='booking_id') != -1:
        # if booking id already exists
        booking_id = booking_id = random.randint(1, 999999)  # try another random set of numbers

    # to get booking duration and any special request from user
    booking_duration = input('Please enter the duration of your stay (1 night minimum, 30 nights maximum):\n')
    while not is_integer(booking_duration, num_range=[1, 30]):
        booking_duration = input("Enter a VALID NUMBER from 1 to 30")

    special_req = input("Please enter any special requests you might have or press enter to complete booking:\n")

    selected_place = Booking(booking_id)
    selected_place.add_to_db(booking_duration, place_data, special_req)


def _print_booking(booking, special_line=None):
    print(f"*{booking['accom_name'].upper()}*")
    print(f"booking id: {booking['booking_id']}")
    print(f"duration: {booking['duration']} day(s)")
    print(f"special request: '{booking['special_req']}'")
    if special_line is not None:
        print(f"{special_line}")

    print("")


def show_all_bookings(show_end_booking_opt=False):
    # show_booking_opt=true will add a number and a prompt to the accommodation prints for user to enter and book that accommodation
    bookings = storage.load_data('bookings')
    current_index = 0
    for i in bookings:
        _print_booking(i, special_line=f"*[Enter {current_index + 1} to end this booking]*" if show_end_booking_opt else None)
        current_index += 1

    return bookings


def end_booking():
    # prints a list of bookings, user enters number that corresponds to a booking and ends it, increasing rooms available by 1
    # initial prompt to prepare the user
    input("Press enter to see a list of bookings, then enter the number of the booking you want to end.")
    bookings = show_all_bookings(True)

    selected_booking = input("Please enter the number of the booking you want to remove:\n")
    while not is_integer(selected_booking, [1, len(bookings)]):
        selected_booking = input("Please enter a VALID NUMBER of the booking you want to remove:\n")

    selected_booking = bookings[int(selected_booking) - 1]
    confirmation = input(f"Are you sure you want to end this booking for {selected_booking['accom_name'].upper()}? (Y/N)")
    if confirmation.lower() == 'y':
        storage.remove_data('bookings', key='booking_id', value=selected_booking['booking_id'])
        place = Place(selected_booking['accom_name'])
        place.remove_booking()
