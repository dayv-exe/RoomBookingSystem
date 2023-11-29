# THIS MODULE HANDLES PLACES LISTED ON THE APP
import os
from algo import sort
from algo import type_validation
from algo import storage
from algo import search


class Places:
    PLACES_PATH = "data/places.csv"  # the file path for places
    PLACES_CSV_HEADER = "name, type, address, available_rooms, price"  # the header for places csv file

    def __init__(self):
        # list of valid accommodation types
        self.ACCOMMODATION_TYPES = sort.sort_array(["Hotel", "Hostel", "Bed and breakfast", "Apartment", "Guest house", "Dormitory", "Campsite", "Motel", "Cottage", "Resort", "Villa", "Inn", "Chalet", "Lodge", "Homestay", "Log cabin", "Glamping"], 0, 16)

    def places_csv_exists(self):
        # to check if places csv exists
        return os.path.isfile(self.PLACES_PATH)

    def valid_accommodation_type(self, user_input):
        # CHECKS IF THE ACCOMMODATION TYPE THE USERS HAS ENTERED CORRESPONDS WITH ANY VALID ACCOM. TYPE

        # type validation
        user_input = type_validation.is_integer(user_input)
        if user_input is False:
            return False

        # index range validation
        if user_input < 1 or user_input > len(self.ACCOMMODATION_TYPES):
            return False

        # assign accommodation type
        chosen_type = self.ACCOMMODATION_TYPES[user_input - 1]
        return search.binary_search(self.ACCOMMODATION_TYPES, chosen_type) != -1

    def add_new_place(self):
        # prompts user to enter the name, accommodation type, address, available rooms, and cost per night of stay for a new place they want to add

        # initial prompt to prepare the user
        input("We will need a few details about the place\nlike name, accommodation type, address, available rooms, and cost per night of stay.\nPress enter to continue")
        print("\n")

        # to get a valid name longer than 1 char and that does not already exist
        np_name = input("Please enter a name for this new place:\n")
        while len(np_name) < 2 or search.binary_search_places(storage.sort_places(self.PLACES_PATH, 0), 0, np_name.lower()) != -1:
            np_name = input("The name you entered is not valid or has already been used, try another:\n")

        # to print out a list of valid accommodation types and prompt the user to select
        type_index = 0
        for t in self.ACCOMMODATION_TYPES:
            type_index += 1
            print(f"{type_index}. {t}")
        print(f"What type of place would {np_name} be?")
        np_type = ""
        while not self.valid_accommodation_type(np_type):
            np_type = input("*Select a valid accommodation type from list (enter number)*: ")

        # to get an address for the accommodation
        np_address = input(f"Where would {np_name} be located?:\n")
        while len(np_address) < 2:
            np_address = input(f"Please enter a valid address for {np_name}:\n")

        # to set the initial available rooms for the accommodation
        np_available_rooms = input(f"How many rooms will be available initially?:\n")
        while not type_validation.is_integer(np_available_rooms):
            np_available_rooms = input(f"Please enter a number greater than 0 for initial rooms available at {np_name}:\n")

        # to set the price per night of the accommodation
        np_price_per_night = input(f"Lastly, how much would {np_name} cost per night:\n")
        while not type_validation.is_integer(np_price_per_night):
            np_price_per_night = input(f"Please enter a number greater than 0 for {np_name}'s price per night\n")

        # to store the new accommodation
        storage.append_data(self.PLACES_PATH, f"{np_name.lower()},{np_type},{np_address.lower()},{abs(int(np_available_rooms))},{abs(int(np_price_per_night))}")
        print(f"Successfully added {np_name} to list")
