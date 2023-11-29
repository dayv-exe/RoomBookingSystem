# THIS MODULE HANDLES PLACES LISTED ON THE APP
from algo import sort
from algo import search
from algo import type_validation
from algo import storage


class Places:
    PLACES_PATH = "data/places.csv"

    def __init__(self):
        # list of valid accommodation types
        self.ACCOMMODATION_TYPES = sort.sort_array(["Hotel", "Hostel", "Bed and breakfast", "Apartment", "Guest house", "Dormitory", "Campsite", "Motel", "Cottage", "Resort", "Villa", "Inn", "Chalet", "Lodge", "Homestay", "Log cabin", "Glamping"], 0, 16)

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

        # to get a valid name longer than 1 char
        np_name = ""
        while len(np_name) < 2:
            np_name = input("Please enter a valid name for this new place:\n")

        # to print out a list of valid accommodation types and prompt the user to select
        type_index = 0
        for t in self.ACCOMMODATION_TYPES:
            type_index += 1
            print(f"{type_index}. {t}")
        print(f"What type of place would {np_name} be?")
        np_type = ""
        while not self.valid_accommodation_type(np_type):
            np_type = input("*Select a valid accommodation type from list (enter number)*: ")

        np_address = input(f"Where would {np_name} be located?:\n")
        while len(np_address) < 2:
            np_address = input(f"Please enter a valid address for {np_name}:\n")

        np_available_rooms = input(f"How many rooms will be available initially?:\n")
        while not type_validation.is_integer(np_available_rooms):
            np_available_rooms = input(f"Please enter a number greater than 0 for initial rooms available at {np_name}:\n")

        np_price_per_night = input(f"Lastly, how much would {np_name} cost per night:\n")
        while not type_validation.is_integer(np_price_per_night):
            np_price_per_night = input(f"Please enter a number greater than 0 for {np_name}'s price per night\n")

        storage.add_to(self.PLACES_PATH, f"{np_name}, {np_type}, {np_address},{np_available_rooms}, {np_price_per_night}")
        print(f"Successfully added {np_name} to list")
