# THIS MODULE HANDLES PLACES LISTED ON THE APP
import storage
from functions import type_validation, sort, search
from classes.place import Place


PLACES_PATH = "data/data.json"  # the file path for places
ACCOMMODATION_TYPES = sort.sort_array(["Hotel", "Hostel", "Bed and breakfast", "Apartment", "Guest house", "Dormitory", "Campsite", "Motel", "Cottage", "Resort", "Villa", "Inn", "Chalet", "Lodge", "Homestay", "Log cabin", "Glamping"], 0, 16)


def valid_accommodation_type(user_input):
    # CHECKS IF THE ACCOMMODATION TYPE THE USERS HAS ENTERED CORRESPONDS WITH ANY VALIDACCOM. TYPE

    # type validation
    user_input = type_validation.is_integer(user_input)
    if user_input is False:
        return False

    # index range validation
    if user_input < 1 or user_input > len(ACCOMMODATION_TYPES):
        return False

    # assign accommodation type
    chosen_type = ACCOMMODATION_TYPES[user_input - 1]
    return search.binary_search(ACCOMMODATION_TYPES, chosen_type) != -1


def search_place():
    # THIS FUNC RETURNS A PLACE AND ALL ITS DETAILS IF NAME USER PROVIDED MATCHES A NAME IN DB
    # ELSE FUNC RETURNS 'None'

    # get list of places in db and sorts them according to name
    existing_places = storage.load_data('places')
    existing_places = sort.sort_places_array(existing_places, 'name', 0, len(existing_places) - 1)

    while True:
        place = input("Please enter the name of the place you want to search for:\n")
        while len(place) < 2:
            place = input("Please enter a VALID name for the place you want to search for:\n")
        place_found = search.binary_search_places(existing_places, place, 'name')
        if place_found != -1:
            print(f"**FOUND**")
            print(f"Name: {place_found['name']}")
            print(f"Type: {place_found['type']}")
            print(f"Address: {place_found['address']}")
            print(f"Available rooms: {place_found['available_rooms']}")
            print(f"Price per night: {place_found['cost_per_night']}")
            retry = input(f"\nDo you want to search again? (Y/N)")
            if retry.lower() == "n":
                break

        else:
            retry = input("No results!\nTry again (Y/N)")
            if retry.lower() == 'n':
                break


def add_new_place():
    # prompts user to enter the name, accommodation type, address, available rooms, and cost per night of stay for a new place they want to add

    # get list of places in db and sorts them according to name
    existing_places = storage.load_data('places')
    existing_places = sort.sort_places_array(existing_places, 'name', 0, len(existing_places) - 1)

    # initial prompt to prepare the user
    input("We will need a few details about the place\nlike name, accommodation type, address, available rooms, and cost per night of stay.\nPress enter to continue")
    print("\n")

    # to get a valid name longer than 1 char and that does not already exist
    np_name = input("Please enter a name for this new place:\n")

    # searches sorted list from earlier to see if name user entered already exists
    while len(np_name) < 2 or search.binary_search_places(existing_places, np_name.lower(), 'name') != -1:
        np_name = input("The name you entered is not valid or has already been used, try another:\n")
    # to print out a list of valid accommodation types and prompt the user to select
    type_index = 0
    for t in ACCOMMODATION_TYPES:
        type_index += 1
        print(f"{type_index}. {t}")
    print(f"What type of place would {np_name} be?")
    np_type = ""
    while not valid_accommodation_type(np_type):
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
    new_place = Place(np_name)
    new_place.add_to_db(np_type, np_address, np_available_rooms, np_price_per_night)

    return f"Successfully added {np_name} to list"
